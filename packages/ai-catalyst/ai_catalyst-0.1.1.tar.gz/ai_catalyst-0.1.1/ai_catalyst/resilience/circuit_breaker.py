"""
Circuit Breaker pattern for fault tolerance
"""

import asyncio
import time
from typing import Callable, Any, Optional
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class CircuitState(Enum):
    """Circuit breaker states"""
    CLOSED = "closed"      # Normal operation
    OPEN = "open"          # Circuit is open, failing fast
    HALF_OPEN = "half_open"  # Testing if service recovered


@dataclass
class CircuitBreakerConfig:
    """Circuit breaker configuration"""
    failure_threshold: int = 5
    recovery_timeout: float = 60.0
    expected_exception: type = Exception
    success_threshold: int = 3  # Successes needed to close from half-open


class CircuitBreaker:
    """Circuit breaker for fault tolerance"""
    
    def __init__(self, config: Optional[CircuitBreakerConfig] = None):
        """
        Initialize circuit breaker
        
        Args:
            config: Circuit breaker configuration
        """
        self.config = config or CircuitBreakerConfig()
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None
        self._lock = asyncio.Lock()
    
    async def call_async(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute function through circuit breaker (async)
        
        Args:
            func: Function to execute
            *args: Function arguments
            **kwargs: Function keyword arguments
            
        Returns:
            Function result
            
        Raises:
            CircuitBreakerOpenError: If circuit is open
            Exception: Original exception from function
        """
        async with self._lock:
            # Check if circuit should transition from open to half-open
            if self.state == CircuitState.OPEN:
                if self._should_attempt_reset():
                    self.state = CircuitState.HALF_OPEN
                    self.success_count = 0
                    logger.info("Circuit breaker transitioning to HALF_OPEN")
                else:
                    raise CircuitBreakerOpenError(
                        f"Circuit breaker is OPEN. Last failure: {self.last_failure_time}"
                    )
        
        try:
            # Execute the function
            if asyncio.iscoroutinefunction(func):
                result = await func(*args, **kwargs)
            else:
                result = func(*args, **kwargs)
            
            # Handle success
            await self._on_success()
            return result
            
        except Exception as e:
            # Handle failure
            await self._on_failure(e)
            raise
    
    def call_sync(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute function through circuit breaker (sync)
        
        Args:
            func: Function to execute
            *args: Function arguments
            **kwargs: Function keyword arguments
            
        Returns:
            Function result
        """
        return asyncio.run(self.call_async(func, *args, **kwargs))
    
    async def _on_success(self):
        """Handle successful function execution"""
        async with self._lock:
            self.failure_count = 0
            
            if self.state == CircuitState.HALF_OPEN:
                self.success_count += 1
                if self.success_count >= self.config.success_threshold:
                    self.state = CircuitState.CLOSED
                    logger.info("Circuit breaker CLOSED after successful recovery")
    
    async def _on_failure(self, exception: Exception):
        """Handle failed function execution"""
        async with self._lock:
            # Only count expected exceptions as failures
            if isinstance(exception, self.config.expected_exception):
                self.failure_count += 1
                self.last_failure_time = time.time()
                
                if self.state == CircuitState.HALF_OPEN:
                    # Failure during half-open immediately opens circuit
                    self.state = CircuitState.OPEN
                    logger.warning("Circuit breaker OPEN after failure during HALF_OPEN")
                elif self.failure_count >= self.config.failure_threshold:
                    # Too many failures, open the circuit
                    self.state = CircuitState.OPEN
                    logger.warning(f"Circuit breaker OPEN after {self.failure_count} failures")
    
    def _should_attempt_reset(self) -> bool:
        """Check if circuit should attempt to reset"""
        if self.last_failure_time is None:
            return True
        
        return (time.time() - self.last_failure_time) >= self.config.recovery_timeout
    
    def get_state(self) -> CircuitState:
        """Get current circuit state"""
        return self.state
    
    def get_stats(self) -> dict:
        """Get circuit breaker statistics"""
        return {
            'state': self.state.value,
            'failure_count': self.failure_count,
            'success_count': self.success_count,
            'last_failure_time': self.last_failure_time,
            'failure_threshold': self.config.failure_threshold,
            'recovery_timeout': self.config.recovery_timeout
        }
    
    def reset(self):
        """Manually reset circuit breaker to closed state"""
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = None
        logger.info("Circuit breaker manually reset to CLOSED")
    
    def force_open(self):
        """Manually open circuit breaker"""
        self.state = CircuitState.OPEN
        self.last_failure_time = time.time()
        logger.warning("Circuit breaker manually forced OPEN")


class CircuitBreakerOpenError(Exception):
    """Exception raised when circuit breaker is open"""
    pass


# Decorator for easy circuit breaker functionality
def circuit_breaker(config: Optional[CircuitBreakerConfig] = None):
    """
    Decorator to add circuit breaker functionality to functions
    
    Args:
        config: Circuit breaker configuration
        
    Returns:
        Decorated function
    """
    breaker = CircuitBreaker(config)
    
    def decorator(func):
        if asyncio.iscoroutinefunction(func):
            async def async_wrapper(*args, **kwargs):
                return await breaker.call_async(func, *args, **kwargs)
            return async_wrapper
        else:
            def sync_wrapper(*args, **kwargs):
                return breaker.call_sync(func, *args, **kwargs)
            return sync_wrapper
    
    return decorator


# Predefined circuit breaker configurations
CIRCUIT_BREAKER_CONFIGS = {
    'api_service': CircuitBreakerConfig(
        failure_threshold=5,
        recovery_timeout=60.0,
        expected_exception=Exception,
        success_threshold=3
    ),
    'database': CircuitBreakerConfig(
        failure_threshold=3,
        recovery_timeout=30.0,
        expected_exception=Exception,
        success_threshold=2
    ),
    'external_service': CircuitBreakerConfig(
        failure_threshold=10,
        recovery_timeout=120.0,
        expected_exception=Exception,
        success_threshold=5
    ),
    'llm_provider': CircuitBreakerConfig(
        failure_threshold=3,
        recovery_timeout=180.0,  # LLM services may need longer recovery
        expected_exception=Exception,
        success_threshold=2
    )
}