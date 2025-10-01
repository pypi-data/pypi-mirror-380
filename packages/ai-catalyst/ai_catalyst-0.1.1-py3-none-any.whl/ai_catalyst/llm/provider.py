"""
LLM Provider - Three-tier LLM system with automatic failover

Supports:
- Local LLM endpoints (LM Studio, Ollama)
- Network LLM endpoints
- OpenAI API
"""

import json
import os
import asyncio
from typing import Dict, List, Optional, Any
from openai import AsyncOpenAI
import aiohttp
from ..security import APIKeyVault, RateLimiter, AuditLogger
from ..security.rate_limiter import PROVIDER_LIMITS
from ..resilience import RetryHandler, CircuitBreaker
from ..resilience.retry_handler import RETRY_CONFIGS
from ..resilience.circuit_breaker import CIRCUIT_BREAKER_CONFIGS


class LLMProvider:
    """Three-tier LLM provider with automatic endpoint discovery and failover"""
    
    def __init__(self, config: Optional[Dict] = None, 
                 key_vault: Optional[APIKeyVault] = None,
                 rate_limiter: Optional[RateLimiter] = None,
                 audit_logger: Optional[AuditLogger] = None):
        """
        Initialize LLM provider
        
        Args:
            config: Configuration dict with optional keys:
                - openai_api_key: OpenAI API key (or use OPENAI_API_KEY env var)
                - network_url: Network LLM endpoint URL
                - timeout: Request timeout in seconds (default: 30)
                - model: Default model name (default: gpt-3.5-turbo)
        """
        self.config = config or {}
        self.timeout = self.config.get('timeout', 30)
        self.default_model = self.config.get('model', 'gpt-3.5-turbo')
        
        # Security components
        self.key_vault = key_vault or APIKeyVault()
        self.rate_limiter = rate_limiter or RateLimiter()
        self.audit_logger = audit_logger or AuditLogger(enable_console=False)
        
        # Resilience components
        self.retry_handler = RetryHandler(RETRY_CONFIGS['api_calls'])
        self.circuit_breakers = {
            'openai': CircuitBreaker(CIRCUIT_BREAKER_CONFIGS['llm_provider']),
            'local': CircuitBreaker(CIRCUIT_BREAKER_CONFIGS['llm_provider']),
            'network': CircuitBreaker(CIRCUIT_BREAKER_CONFIGS['llm_provider'])
        }
        
        # Initialize OpenAI client with key vault
        openai_key = self.key_vault.get_key('openai') or os.getenv('OPENAI_API_KEY')
        self.openai_client = AsyncOpenAI(api_key=openai_key) if openai_key else None
        self._session = None
        
        # Cache discovered endpoints
        self._local_endpoints = None
        
        # Setup rate limits
        self._setup_rate_limits()
        
    async def discover_local_endpoints(self) -> List[str]:
        """Discover local LLM endpoints"""
        if self._local_endpoints is not None:
            return self._local_endpoints
            
        endpoints = []
        ports = [8000, 8080, 11434, 5000, 7860, 1234]
        
        async with self._get_session() as session:
            for port in ports:
                try:
                    async with session.get(f"http://localhost:{port}/v1/models", timeout=aiohttp.ClientTimeout(total=2)) as response:
                        if response.status == 200:
                            endpoints.append(f"http://localhost:{port}/v1")
                except:
                    continue
        
        self._local_endpoints = endpoints
        return endpoints
    
    async def generate_async(self, 
                prompt: str, 
                provider: str = "auto",
                model: Optional[str] = None,
                temperature: float = 0.7,
                max_tokens: Optional[int] = None) -> Dict[str, Any]:
        """
        Generate text using specified provider
        
        Args:
            prompt: Input prompt
            provider: Provider type ("local", "network", "openai", "auto")
            model: Model name (uses default if not specified)
            temperature: Generation temperature
            max_tokens: Maximum tokens to generate
            
        Returns:
            Dict with keys: content, provider_used, error
        """
        if provider == "auto":
            # Try providers concurrently, return first success
            tasks = []
            if await self.is_available_async("local"):
                tasks.append(self._generate_with_timeout("local", prompt, model, temperature, max_tokens))
            if await self.is_available_async("network"):
                tasks.append(self._generate_with_timeout("network", prompt, model, temperature, max_tokens))
            if await self.is_available_async("openai"):
                tasks.append(self._generate_with_timeout("openai", prompt, model, temperature, max_tokens))
            
            if not tasks:
                return {"content": None, "provider_used": None, "error": "No providers available"}
            
            for completed_task in asyncio.as_completed(tasks):
                result = await completed_task
                if not result.get("error"):
                    # Cancel remaining tasks
                    for task in tasks:
                        if not task.done():
                            task.cancel()
                    return result
            
            return {"content": None, "provider_used": None, "error": "All providers failed"}
        
        elif provider == "local":
            return await self._generate_local(prompt, model, temperature, max_tokens)
        elif provider == "network":
            return await self._generate_network(prompt, model, temperature, max_tokens)
        elif provider == "openai":
            return await self._generate_openai(prompt, model, temperature, max_tokens)
        else:
            return {"content": None, "provider_used": None, "error": f"Unknown provider: {provider}"}
    
    async def _generate_local(self, prompt: str, model: Optional[str], temperature: float, max_tokens: Optional[int]) -> Dict[str, Any]:
        """Generate using local LLM endpoint"""
        endpoints = await self.discover_local_endpoints()
        if not endpoints:
            return {"content": None, "provider_used": "local", "error": "No local LLM endpoints found"}
        
        return await self._generate_with_endpoint(endpoints[0], prompt, model, temperature, max_tokens, "local")
    
    async def _generate_network(self, prompt: str, model: Optional[str], temperature: float, max_tokens: Optional[int]) -> Dict[str, Any]:
        """Generate using network LLM endpoint"""
        network_url = self.config.get('network_url')
        if not network_url:
            return {"content": None, "provider_used": "network", "error": "No network URL configured"}
        
        return await self._generate_with_endpoint(network_url, prompt, model, temperature, max_tokens, "network")
    
    async def _generate_openai(self, prompt: str, model: Optional[str], temperature: float, max_tokens: Optional[int]) -> Dict[str, Any]:
        """Generate using OpenAI API"""
        if not self.openai_client:
            return {"content": None, "provider_used": "openai", "error": "No OpenAI API key configured"}
        
        try:
            response = await self.openai_client.chat.completions.create(
                model=model or "gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
                max_tokens=max_tokens
            )
            
            content = response.choices[0].message.content.strip()
            return {"content": content, "provider_used": "openai", "error": None}
            
        except Exception as e:
            error_msg = str(e)
            if "401" in error_msg or "invalid_api_key" in error_msg:
                error_msg = "Invalid OpenAI API key"
            return {"content": None, "provider_used": "openai", "error": error_msg}
    
    async def _generate_with_endpoint(self, endpoint_url: str, prompt: str, model: Optional[str], 
                               temperature: float, max_tokens: Optional[int], provider_name: str) -> Dict[str, Any]:
        """Generate using OpenAI-compatible endpoint"""
        try:
            payload = {
                "model": model or self.default_model,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": temperature
            }
            
            if max_tokens:
                payload["max_tokens"] = max_tokens
            
            async with self._get_session() as session:
                async with session.post(
                    f"{endpoint_url}/chat/completions",
                    json=payload,
                    timeout=aiohttp.ClientTimeout(total=self.timeout)
                ) as response:
                    
                    if response.status != 200:
                        text = await response.text()
                        return {
                            "content": None, 
                            "provider_used": provider_name, 
                            "error": f"HTTP {response.status}: {text[:100]}"
                        }
                    
                    result = await response.json()
            content = result["choices"][0]["message"]["content"].strip()
            return {"content": content, "provider_used": provider_name, "error": None}
            
        except Exception as e:
            return {"content": None, "provider_used": provider_name, "error": str(e)}
    
    async def is_available_async(self, provider: str) -> bool:
        """Check if a provider is available"""
        if provider == "local":
            endpoints = await self.discover_local_endpoints()
            return len(endpoints) > 0
        elif provider == "network":
            return bool(self.config.get('network_url'))
        elif provider == "openai":
            return self.openai_client is not None
        else:
            return False
    
    async def get_available_providers_async(self) -> List[str]:
        """Get list of available providers"""
        providers = []
        if await self.is_available_async("local"):
            providers.append("local")
        if await self.is_available_async("network"):
            providers.append("network")
        if await self.is_available_async("openai"):
            providers.append("openai")
        return providers
    
    def _setup_rate_limits(self):
        """Setup rate limits for providers"""
        # Set rate limits based on provider type
        provider_configs = {
            'openai': 'openai_paid',  # Assume paid by default
            'local': 'local_llm',
            'network': 'local_llm'
        }
        
        for provider, limit_type in provider_configs.items():
            if limit_type in PROVIDER_LIMITS:
                self.rate_limiter.set_limit(provider, PROVIDER_LIMITS[limit_type])
    
    def _get_session(self):
        """Get or create aiohttp session"""
        if self._session is None or self._session.closed:
            self._session = aiohttp.ClientSession()
        return self._session
    
    async def _generate_with_timeout(self, provider: str, prompt: str, model: Optional[str], 
                                   temperature: float, max_tokens: Optional[int]) -> Dict[str, Any]:
        """Generate with timeout wrapper for concurrent execution"""
        try:
            if provider == "local":
                return await self._generate_local(prompt, model, temperature, max_tokens)
            elif provider == "network":
                return await self._generate_network(prompt, model, temperature, max_tokens)
            elif provider == "openai":
                return await self._generate_openai(prompt, model, temperature, max_tokens)
        except asyncio.TimeoutError:
            return {"content": None, "provider_used": provider, "error": "Request timeout"}
        except Exception as e:
            return {"content": None, "provider_used": provider, "error": str(e)}
    
    async def close(self):
        """Close HTTP session"""
        if self._session and not self._session.closed:
            await self._session.close()
    
    # Sync compatibility wrappers
    def generate(self, prompt: str, provider: str = "auto", model: Optional[str] = None,
                temperature: float = 0.7, max_tokens: Optional[int] = None) -> Dict[str, Any]:
        """Sync wrapper for generate_async"""
        return asyncio.run(self.generate_async(prompt, provider, model, temperature, max_tokens))
    
    def is_available(self, provider: str) -> bool:
        """Sync wrapper for is_available_async"""
        return asyncio.run(self.is_available_async(provider))
    
    def get_available_providers(self) -> List[str]:
        """Sync wrapper for get_available_providers_async"""
        return asyncio.run(self.get_available_providers_async())