"""
API Key Vault for secure key management and rotation
"""

import os
import json
import time
from typing import Dict, Optional, List, Any
from datetime import datetime, timedelta
from .config_vault import SecureConfigManager
import logging

logger = logging.getLogger(__name__)


class APIKeyVault:
    """Secure API key management with rotation capabilities"""
    
    def __init__(self, config_manager: Optional[SecureConfigManager] = None):
        """
        Initialize API key vault
        
        Args:
            config_manager: Secure config manager for encryption
        """
        self.config_manager = config_manager or SecureConfigManager()
        self._keys = {}
        self._key_metadata = {}
        self._load_keys_from_env()
    
    def _load_keys_from_env(self):
        """Load API keys from environment variables"""
        env_mappings = {
            'openai': 'OPENAI_API_KEY',
            'anthropic': 'ANTHROPIC_API_KEY',
            'azure_openai': 'AZURE_OPENAI_API_KEY',
            'huggingface': 'HUGGINGFACE_API_KEY',
            'cohere': 'COHERE_API_KEY'
        }
        
        for provider, env_var in env_mappings.items():
            key = os.getenv(env_var)
            if key:
                self.store_key(provider, key, source='environment')
    
    def store_key(self, provider: str, api_key: str, 
                  source: str = 'manual', 
                  expires_at: Optional[datetime] = None,
                  metadata: Optional[Dict[str, Any]] = None) -> bool:
        """
        Store an API key securely
        
        Args:
            provider: Provider name (e.g., 'openai', 'anthropic')
            api_key: The API key to store
            source: Source of the key ('environment', 'manual', 'rotation')
            expires_at: Optional expiration datetime
            metadata: Additional metadata
            
        Returns:
            True if stored successfully
        """
        try:
            # Encrypt the key
            encrypted_data = self.config_manager.set_secure(
                f"{provider}_api_key", 
                api_key, 
                encrypt=True
            )
            
            self._keys[provider] = encrypted_data
            self._key_metadata[provider] = {
                'created_at': datetime.now().isoformat(),
                'source': source,
                'expires_at': expires_at.isoformat() if expires_at else None,
                'last_used': None,
                'usage_count': 0,
                'metadata': metadata or {}
            }
            
            logger.info(f"Stored API key for provider: {provider}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to store API key for {provider}: {e}")
            return False
    
    def get_key(self, provider: str) -> Optional[str]:
        """
        Retrieve an API key
        
        Args:
            provider: Provider name
            
        Returns:
            Decrypted API key or None if not found/expired
        """
        if provider not in self._keys:
            return None
        
        # Check expiration
        metadata = self._key_metadata.get(provider, {})
        expires_at = metadata.get('expires_at')
        if expires_at:
            expiry_time = datetime.fromisoformat(expires_at)
            if datetime.now() > expiry_time:
                logger.warning(f"API key for {provider} has expired")
                return None
        
        try:
            # Decrypt and return key
            key = self.config_manager.get_secure(self._keys[provider])
            
            # Update usage metadata
            self._key_metadata[provider]['last_used'] = datetime.now().isoformat()
            self._key_metadata[provider]['usage_count'] += 1
            
            return key
            
        except Exception as e:
            logger.error(f"Failed to retrieve API key for {provider}: {e}")
            return None
    
    def rotate_key(self, provider: str, new_api_key: str) -> bool:
        """
        Rotate an API key
        
        Args:
            provider: Provider name
            new_api_key: New API key
            
        Returns:
            True if rotation successful
        """
        # Store old key metadata for audit
        old_metadata = self._key_metadata.get(provider, {})
        
        # Store new key
        success = self.store_key(
            provider, 
            new_api_key, 
            source='rotation',
            metadata={'previous_rotation': old_metadata.get('created_at')}
        )
        
        if success:
            logger.info(f"Rotated API key for provider: {provider}")
        
        return success
    
    def delete_key(self, provider: str) -> bool:
        """
        Delete an API key
        
        Args:
            provider: Provider name
            
        Returns:
            True if deleted successfully
        """
        if provider in self._keys:
            del self._keys[provider]
            del self._key_metadata[provider]
            logger.info(f"Deleted API key for provider: {provider}")
            return True
        return False
    
    def list_providers(self) -> List[str]:
        """List all providers with stored keys"""
        return list(self._keys.keys())
    
    def get_key_info(self, provider: str) -> Optional[Dict[str, Any]]:
        """
        Get metadata about a stored key
        
        Args:
            provider: Provider name
            
        Returns:
            Key metadata (without the actual key)
        """
        if provider not in self._key_metadata:
            return None
        
        info = self._key_metadata[provider].copy()
        info['provider'] = provider
        info['has_key'] = provider in self._keys
        
        # Check if expired
        expires_at = info.get('expires_at')
        if expires_at:
            expiry_time = datetime.fromisoformat(expires_at)
            info['is_expired'] = datetime.now() > expiry_time
        else:
            info['is_expired'] = False
        
        return info
    
    def validate_key(self, provider: str, test_endpoint: Optional[str] = None) -> bool:
        """
        Validate an API key by making a test request
        
        Args:
            provider: Provider name
            test_endpoint: Optional test endpoint URL
            
        Returns:
            True if key is valid
        """
        key = self.get_key(provider)
        if not key:
            return False
        
        # Provider-specific validation
        if provider == 'openai':
            return self._validate_openai_key(key)
        elif provider == 'anthropic':
            return self._validate_anthropic_key(key)
        else:
            # Generic validation if test_endpoint provided
            if test_endpoint:
                return self._validate_generic_key(key, test_endpoint)
        
        return True  # Assume valid if no validation method
    
    def _validate_openai_key(self, api_key: str) -> bool:
        """Validate OpenAI API key"""
        try:
            import openai
            client = openai.OpenAI(api_key=api_key)
            # Test with a minimal request
            client.models.list()
            return True
        except Exception as e:
            logger.warning(f"OpenAI key validation failed: {e}")
            return False
    
    def _validate_anthropic_key(self, api_key: str) -> bool:
        """Validate Anthropic API key"""
        try:
            import requests
            headers = {
                'x-api-key': api_key,
                'anthropic-version': '2023-06-01'
            }
            response = requests.get(
                'https://api.anthropic.com/v1/messages',
                headers=headers,
                timeout=5
            )
            # 401 means invalid key, other errors might be valid key with wrong request
            return response.status_code != 401
        except Exception as e:
            logger.warning(f"Anthropic key validation failed: {e}")
            return False
    
    def _validate_generic_key(self, api_key: str, endpoint: str) -> bool:
        """Generic API key validation"""
        try:
            import requests
            headers = {'Authorization': f'Bearer {api_key}'}
            response = requests.get(endpoint, headers=headers, timeout=5)
            return response.status_code != 401
        except Exception as e:
            logger.warning(f"Generic key validation failed: {e}")
            return False
    
    def export_vault(self, include_keys: bool = False) -> str:
        """
        Export vault configuration
        
        Args:
            include_keys: Whether to include encrypted keys (for backup)
            
        Returns:
            JSON string of vault data
        """
        export_data = {
            'metadata': self._key_metadata,
            'exported_at': datetime.now().isoformat()
        }
        
        if include_keys:
            export_data['keys'] = self._keys
        
        return json.dumps(export_data)
    
    def import_vault(self, vault_json: str, overwrite: bool = False) -> bool:
        """
        Import vault configuration
        
        Args:
            vault_json: JSON string of vault data
            overwrite: Whether to overwrite existing keys
            
        Returns:
            True if import successful
        """
        try:
            data = json.loads(vault_json)
            
            # Import metadata
            for provider, metadata in data.get('metadata', {}).items():
                if provider not in self._key_metadata or overwrite:
                    self._key_metadata[provider] = metadata
            
            # Import keys if present
            if 'keys' in data:
                for provider, key_data in data['keys'].items():
                    if provider not in self._keys or overwrite:
                        self._keys[provider] = key_data
            
            logger.info("Vault import completed successfully")
            return True
            
        except Exception as e:
            logger.error(f"Vault import failed: {e}")
            return False
    
    def cleanup_expired_keys(self) -> int:
        """
        Remove expired keys
        
        Returns:
            Number of keys removed
        """
        removed_count = 0
        current_time = datetime.now()
        
        providers_to_remove = []
        for provider, metadata in self._key_metadata.items():
            expires_at = metadata.get('expires_at')
            if expires_at:
                expiry_time = datetime.fromisoformat(expires_at)
                if current_time > expiry_time:
                    providers_to_remove.append(provider)
        
        for provider in providers_to_remove:
            self.delete_key(provider)
            removed_count += 1
        
        if removed_count > 0:
            logger.info(f"Cleaned up {removed_count} expired keys")
        
        return removed_count