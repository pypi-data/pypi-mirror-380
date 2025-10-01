"""
Rate Limiter with token bucket algorithm for API throttling
"""

import time
import asyncio
from typing import Dict, Optional, Tuple
from dataclasses import dataclass
from collections import defaultdict
import logging

logger = logging.getLogger(__name__)


@dataclass
class RateLimit:
    """Rate limit configuration"""
    requests_per_minute: int
    requests_per_hour: int
    requests_per_day: int
    burst_size: Optional[int] = None
    
    def __post_init__(self):
        if self.burst_size is None:
            self.burst_size = min(self.requests_per_minute, 10)


@dataclass
class TokenBucket:
    """Token bucket for rate limiting"""
    capacity: int
    tokens: float
    refill_rate: float  # tokens per second
    last_refill: float
    
    def __post_init__(self):
        self.last_refill = time.time()
    
    def refill(self):
        """Refill tokens based on elapsed time"""
        now = time.time()
        elapsed = now - self.last_refill
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now
    
    def consume(self, tokens: int = 1) -> bool:
        """
        Try to consume tokens
        
        Args:
            tokens: Number of tokens to consume
            
        Returns:
            True if tokens were consumed, False if not enough tokens
        """
        self.refill()
        if self.tokens >= tokens:
            self.tokens -= tokens
            return True
        return False
    
    def time_until_available(self, tokens: int = 1) -> float:
        """
        Calculate time until enough tokens are available
        
        Args:
            tokens: Number of tokens needed
            
        Returns:
            Seconds until tokens are available
        """
        self.refill()
        if self.tokens >= tokens:
            return 0.0
        
        needed_tokens = tokens - self.tokens
        return needed_tokens / self.refill_rate


class RateLimiter:
    """Rate limiter with token bucket algorithm"""
    
    def __init__(self):
        self._buckets: Dict[str, Dict[str, TokenBucket]] = defaultdict(dict)
        self._limits: Dict[str, RateLimit] = {}
        self._global_limits: Dict[str, RateLimit] = {}
        self._usage_stats: Dict[str, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    
    def set_limit(self, identifier: str, rate_limit: RateLimit):
        """
        Set rate limit for a specific identifier
        
        Args:
            identifier: Unique identifier (e.g., 'openai', 'user:123')
            rate_limit: Rate limit configuration
        """
        self._limits[identifier] = rate_limit
        
        # Create token buckets for different time windows
        self._buckets[identifier] = {
            'minute': TokenBucket(
                capacity=rate_limit.burst_size,
                tokens=rate_limit.burst_size,
                refill_rate=rate_limit.requests_per_minute / 60.0,
                last_refill=time.time()
            ),
            'hour': TokenBucket(
                capacity=rate_limit.requests_per_hour,
                tokens=rate_limit.requests_per_hour,
                refill_rate=rate_limit.requests_per_hour / 3600.0,
                last_refill=time.time()
            ),
            'day': TokenBucket(
                capacity=rate_limit.requests_per_day,
                tokens=rate_limit.requests_per_day,
                refill_rate=rate_limit.requests_per_day / 86400.0,
                last_refill=time.time()
            )
        }
        
        logger.info(f"Set rate limit for {identifier}: {rate_limit}")
    
    def set_global_limit(self, limit_type: str, rate_limit: RateLimit):
        """
        Set global rate limit that applies to all requests
        
        Args:
            limit_type: Type of global limit (e.g., 'api', 'llm')
            rate_limit: Rate limit configuration
        """
        self._global_limits[limit_type] = rate_limit
        self.set_limit(f"global:{limit_type}", rate_limit)
    
    def check_limit(self, identifier: str, tokens: int = 1) -> Tuple[bool, Optional[float]]:
        """
        Check if request is within rate limits
        
        Args:
            identifier: Unique identifier
            tokens: Number of tokens to consume
            
        Returns:
            Tuple of (allowed, retry_after_seconds)
        """
        if identifier not in self._buckets:
            # No limit set, allow request
            return True, None
        
        buckets = self._buckets[identifier]
        
        # Check all time windows
        for window, bucket in buckets.items():
            if not bucket.consume(tokens):
                retry_after = bucket.time_until_available(tokens)
                logger.warning(f"Rate limit exceeded for {identifier} ({window}), retry after {retry_after:.2f}s")
                return False, retry_after
        
        # Check global limits
        for limit_type, _ in self._global_limits.items():
            global_id = f"global:{limit_type}"
            if global_id in self._buckets:
                global_buckets = self._buckets[global_id]
                for window, bucket in global_buckets.items():
                    if not bucket.consume(tokens):
                        retry_after = bucket.time_until_available(tokens)
                        logger.warning(f"Global rate limit exceeded ({limit_type}, {window}), retry after {retry_after:.2f}s")
                        return False, retry_after
        
        # Update usage stats
        self._usage_stats[identifier]['total'] += tokens
        self._usage_stats[identifier]['last_request'] = int(time.time())
        
        return True, None
    
    async def wait_for_capacity(self, identifier: str, tokens: int = 1, max_wait: float = 300.0) -> bool:
        """
        Wait until capacity is available
        
        Args:
            identifier: Unique identifier
            tokens: Number of tokens needed
            max_wait: Maximum time to wait in seconds
            
        Returns:
            True if capacity became available, False if timeout
        """
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            allowed, retry_after = self.check_limit(identifier, tokens)
            if allowed:
                return True
            
            if retry_after is None:
                retry_after = 1.0
            
            # Wait for the shorter of retry_after or remaining max_wait
            wait_time = min(retry_after, max_wait - (time.time() - start_time))
            if wait_time > 0:
                await asyncio.sleep(wait_time)
            else:
                break
        
        return False
    
    def get_status(self, identifier: str) -> Dict[str, any]:
        """
        Get current rate limit status
        
        Args:
            identifier: Unique identifier
            
        Returns:
            Status information
        """
        if identifier not in self._buckets:
            return {'error': 'No rate limit configured'}
        
        buckets = self._buckets[identifier]
        status = {}
        
        for window, bucket in buckets.items():
            bucket.refill()
            status[window] = {
                'available_tokens': int(bucket.tokens),
                'capacity': bucket.capacity,
                'refill_rate': bucket.refill_rate,
                'utilization': 1.0 - (bucket.tokens / bucket.capacity)
            }
        
        # Add usage stats
        stats = self._usage_stats.get(identifier, {})
        status['usage'] = {
            'total_requests': stats.get('total', 0),
            'last_request': stats.get('last_request', 0)
        }
        
        return status
    
    def reset_limits(self, identifier: str):
        """Reset rate limits for an identifier"""
        if identifier in self._buckets:
            rate_limit = self._limits[identifier]
            # Recreate buckets with full capacity
            self._buckets[identifier] = {
                'minute': TokenBucket(
                    capacity=rate_limit.burst_size,
                    tokens=rate_limit.burst_size,
                    refill_rate=rate_limit.requests_per_minute / 60.0,
                    last_refill=time.time()
                ),
                'hour': TokenBucket(
                    capacity=rate_limit.requests_per_hour,
                    tokens=rate_limit.requests_per_hour,
                    refill_rate=rate_limit.requests_per_hour / 3600.0,
                    last_refill=time.time()
                ),
                'day': TokenBucket(
                    capacity=rate_limit.requests_per_day,
                    tokens=rate_limit.requests_per_day,
                    refill_rate=rate_limit.requests_per_day / 86400.0,
                    last_refill=time.time()
                )
            }
            logger.info(f"Reset rate limits for {identifier}")
    
    def get_all_status(self) -> Dict[str, Dict[str, any]]:
        """Get status for all configured rate limits"""
        return {identifier: self.get_status(identifier) for identifier in self._buckets.keys()}
    
    def cleanup_expired(self, max_age_hours: int = 24):
        """
        Clean up old rate limit entries
        
        Args:
            max_age_hours: Maximum age in hours before cleanup
        """
        current_time = time.time()
        cutoff_time = current_time - (max_age_hours * 3600)
        
        expired_identifiers = []
        for identifier, stats in self._usage_stats.items():
            last_request = stats.get('last_request', 0)
            if last_request < cutoff_time:
                expired_identifiers.append(identifier)
        
        for identifier in expired_identifiers:
            if identifier in self._buckets:
                del self._buckets[identifier]
            if identifier in self._usage_stats:
                del self._usage_stats[identifier]
            if identifier in self._limits:
                del self._limits[identifier]
        
        if expired_identifiers:
            logger.info(f"Cleaned up {len(expired_identifiers)} expired rate limit entries")


# Predefined rate limits for common providers
PROVIDER_LIMITS = {
    'openai_free': RateLimit(
        requests_per_minute=3,
        requests_per_hour=200,
        requests_per_day=200,
        burst_size=3
    ),
    'openai_paid': RateLimit(
        requests_per_minute=60,
        requests_per_hour=3600,
        requests_per_day=10000,
        burst_size=10
    ),
    'anthropic_free': RateLimit(
        requests_per_minute=5,
        requests_per_hour=1000,
        requests_per_day=1000,
        burst_size=5
    ),
    'anthropic_paid': RateLimit(
        requests_per_minute=50,
        requests_per_hour=4000,
        requests_per_day=40000,
        burst_size=10
    ),
    'local_llm': RateLimit(
        requests_per_minute=30,
        requests_per_hour=1800,
        requests_per_day=10000,
        burst_size=5
    )
}