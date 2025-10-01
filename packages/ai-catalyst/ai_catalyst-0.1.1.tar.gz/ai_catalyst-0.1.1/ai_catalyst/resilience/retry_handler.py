"""
Retry Handler with exponential backoff and jitter
"""

import asyncio
import random
import time
from typing import Callable, Any, Optional, List, Type
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class RetryStrategy(Enum):
    """Retry strategies"""
    EXPONENTIAL_BACKOFF = "exponential_backoff"
    LINEAR_BACKOFF = "linear_backoff"
    FIXED_DELAY = "fixed_delay"


@dataclass
class RetryConfig:
    """Retry configuration"""
    max_attempts: int = 3
    base_delay: float = 1.0
    max_delay: float = 60.0
    strategy: RetryStrategy = RetryStrategy.EXPONENTIAL_BACKOFF
    jitter: bool = True
    backoff_multiplier: float = 2.0
    retryable_exceptions: Optional[List[Type[Exception]]] = None


class RetryHandler:
    """Handles retry logic with various strategies"""
    
    def __init__(self, config: Optional[RetryConfig] = None):
        """
        Initialize retry handler
        
        Args:
            config: Retry configuration
        """
        self.config = config or RetryConfig()
        self._attempt_count = 0
    
    async def execute_async(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute function with retry logic (async)
        
        Args:
            func: Function to execute
            *args: Function arguments
            **kwargs: Function keyword arguments
            
        Returns:
            Function result
            
        Raises:
            Exception: Last exception if all retries failed
        """
        last_exception = None
        
        for attempt in range(self.config.max_attempts):
            self._attempt_count = attempt + 1
            
            try:
                if asyncio.iscoroutinefunction(func):
                    result = await func(*args, **kwargs)
                else:
                    result = func(*args, **kwargs)
                
                if attempt > 0:
                    logger.info(f"Retry succeeded on attempt {attempt + 1}")
                
                return result
                
            except Exception as e:
                last_exception = e
                
                # Check if exception is retryable
                if not self._is_retryable(e):
                    logger.warning(f"Non-retryable exception: {e}")
                    raise e
                
                # Don't delay on last attempt
                if attempt < self.config.max_attempts - 1:
                    delay = self._calculate_delay(attempt)
                    logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay:.2f}s")
                    await asyncio.sleep(delay)
                else:
                    logger.error(f"All {self.config.max_attempts} attempts failed. Last error: {e}")
        
        raise last_exception
    
    def execute_sync(self, func: Callable, *args, **kwargs) -> Any:
        """
        Execute function with retry logic (sync)
        
        Args:
            func: Function to execute
            *args: Function arguments
            **kwargs: Function keyword arguments
            
        Returns:
            Function result
        """
        return asyncio.run(self.execute_async(func, *args, **kwargs))
    
    def _is_retryable(self, exception: Exception) -> bool:
        """
        Check if exception is retryable
        
        Args:
            exception: Exception to check
            
        Returns:
            True if retryable
        """
        if self.config.retryable_exceptions is None:
            # Default retryable exceptions
            retryable_types = (
                ConnectionError,
                TimeoutError,
                OSError,
            )
            
            # Check for common HTTP errors
            if hasattr(exception, 'status_code'):
                # Retry on 5xx errors and some 4xx errors
                status_code = getattr(exception, 'status_code')
                if status_code >= 500 or status_code in [408, 429]:
                    return True
            
            return isinstance(exception, retryable_types)
        
        return isinstance(exception, tuple(self.config.retryable_exceptions))
    
    def _calculate_delay(self, attempt: int) -> float:
        """
        Calculate delay for retry attempt
        
        Args:
            attempt: Current attempt number (0-based)
            
        Returns:
            Delay in seconds
        """
        if self.config.strategy == RetryStrategy.FIXED_DELAY:
            delay = self.config.base_delay
        elif self.config.strategy == RetryStrategy.LINEAR_BACKOFF:
            delay = self.config.base_delay * (attempt + 1)
        else:  # EXPONENTIAL_BACKOFF
            delay = self.config.base_delay * (self.config.backoff_multiplier ** attempt)
        
        # Apply max delay limit
        delay = min(delay, self.config.max_delay)
        
        # Add jitter to prevent thundering herd
        if self.config.jitter:
            jitter_range = delay * 0.1  # 10% jitter
            delay += random.uniform(-jitter_range, jitter_range)
        
        return max(0, delay)
    
    def get_attempt_count(self) -> int:
        """Get current attempt count"""
        return self._attempt_count
    
    def reset(self):
        """Reset attempt counter"""
        self._attempt_count = 0


# Decorator for easy retry functionality
def retry(config: Optional[RetryConfig] = None):
    """
    Decorator to add retry functionality to functions
    
    Args:
        config: Retry configuration
        
    Returns:
        Decorated function
    """
    def decorator(func):
        handler = RetryHandler(config)
        
        if asyncio.iscoroutinefunction(func):
            async def async_wrapper(*args, **kwargs):
                return await handler.execute_async(func, *args, **kwargs)
            return async_wrapper
        else:
            def sync_wrapper(*args, **kwargs):
                return handler.execute_sync(func, *args, **kwargs)
            return sync_wrapper
    
    return decorator


# Predefined retry configurations
RETRY_CONFIGS = {
    'api_calls': RetryConfig(
        max_attempts=3,
        base_delay=1.0,
        max_delay=30.0,
        strategy=RetryStrategy.EXPONENTIAL_BACKOFF,
        jitter=True
    ),
    'database': RetryConfig(
        max_attempts=5,
        base_delay=0.5,
        max_delay=10.0,
        strategy=RetryStrategy.EXPONENTIAL_BACKOFF,
        jitter=True
    ),
    'file_operations': RetryConfig(
        max_attempts=3,
        base_delay=0.1,
        max_delay=5.0,
        strategy=RetryStrategy.LINEAR_BACKOFF,
        jitter=False
    ),
    'network_requests': RetryConfig(
        max_attempts=4,
        base_delay=2.0,
        max_delay=60.0,
        strategy=RetryStrategy.EXPONENTIAL_BACKOFF,
        jitter=True
    )
}