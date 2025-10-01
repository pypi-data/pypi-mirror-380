"""
Health Checker for monitoring service availability
"""

import asyncio
import time
from typing import Dict, List, Callable, Any, Optional
from dataclasses import dataclass
from enum import Enum
import logging

logger = logging.getLogger(__name__)


class HealthStatus(Enum):
    """Health check status"""
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"
    DEGRADED = "degraded"
    UNKNOWN = "unknown"


@dataclass
class HealthCheckResult:
    """Health check result"""
    service_name: str
    status: HealthStatus
    response_time: float
    timestamp: float
    details: Dict[str, Any]
    error_message: Optional[str] = None


@dataclass
class HealthCheckConfig:
    """Health check configuration"""
    interval: float = 30.0  # seconds
    timeout: float = 10.0   # seconds
    failure_threshold: int = 3
    success_threshold: int = 2
    enabled: bool = True


class HealthChecker:
    """Health checker for monitoring services"""
    
    def __init__(self):
        self._checks: Dict[str, Callable] = {}
        self._configs: Dict[str, HealthCheckConfig] = {}
        self._results: Dict[str, List[HealthCheckResult]] = {}
        self._running = False
        self._tasks: List[asyncio.Task] = []
    
    def register_check(self, 
                      service_name: str, 
                      check_func: Callable,
                      config: Optional[HealthCheckConfig] = None):
        """
        Register a health check
        
        Args:
            service_name: Name of the service
            check_func: Function that performs the health check
            config: Health check configuration
        """
        self._checks[service_name] = check_func
        self._configs[service_name] = config or HealthCheckConfig()
        self._results[service_name] = []
        
        logger.info(f"Registered health check for service: {service_name}")
    
    def unregister_check(self, service_name: str):
        """
        Unregister a health check
        
        Args:
            service_name: Name of the service
        """
        if service_name in self._checks:
            del self._checks[service_name]
            del self._configs[service_name]
            del self._results[service_name]
            logger.info(f"Unregistered health check for service: {service_name}")
    
    async def check_service(self, service_name: str) -> HealthCheckResult:
        """
        Perform health check for a specific service
        
        Args:
            service_name: Name of the service
            
        Returns:
            Health check result
        """
        if service_name not in self._checks:
            return HealthCheckResult(
                service_name=service_name,
                status=HealthStatus.UNKNOWN,
                response_time=0.0,
                timestamp=time.time(),
                details={},
                error_message="Service not registered"
            )
        
        check_func = self._checks[service_name]
        config = self._configs[service_name]
        
        start_time = time.time()
        
        try:
            # Execute health check with timeout
            if asyncio.iscoroutinefunction(check_func):
                result = await asyncio.wait_for(check_func(), timeout=config.timeout)
            else:
                result = await asyncio.wait_for(
                    asyncio.to_thread(check_func), 
                    timeout=config.timeout
                )
            
            response_time = time.time() - start_time
            
            # Parse result
            if isinstance(result, dict):
                status = HealthStatus(result.get('status', 'healthy'))
                details = result.get('details', {})
                error_message = result.get('error')
            elif isinstance(result, bool):
                status = HealthStatus.HEALTHY if result else HealthStatus.UNHEALTHY
                details = {}
                error_message = None
            else:
                status = HealthStatus.HEALTHY
                details = {'result': str(result)}
                error_message = None
            
            health_result = HealthCheckResult(
                service_name=service_name,
                status=status,
                response_time=response_time,
                timestamp=time.time(),
                details=details,
                error_message=error_message
            )
            
        except asyncio.TimeoutError:
            health_result = HealthCheckResult(
                service_name=service_name,
                status=HealthStatus.UNHEALTHY,
                response_time=config.timeout,
                timestamp=time.time(),
                details={},
                error_message="Health check timeout"
            )
            
        except Exception as e:
            health_result = HealthCheckResult(
                service_name=service_name,
                status=HealthStatus.UNHEALTHY,
                response_time=time.time() - start_time,
                timestamp=time.time(),
                details={},
                error_message=str(e)
            )
        
        # Store result
        self._results[service_name].append(health_result)
        
        # Keep only recent results (last 100)
        if len(self._results[service_name]) > 100:
            self._results[service_name] = self._results[service_name][-100:]
        
        return health_result
    
    async def check_all_services(self) -> Dict[str, HealthCheckResult]:
        """
        Check all registered services
        
        Returns:
            Dictionary of service names to health check results
        """
        tasks = []
        service_names = []
        
        for service_name in self._checks.keys():
            if self._configs[service_name].enabled:
                tasks.append(self.check_service(service_name))
                service_names.append(service_name)
        
        if not tasks:
            return {}
        
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        return {
            service_name: result if isinstance(result, HealthCheckResult) else 
            HealthCheckResult(
                service_name=service_name,
                status=HealthStatus.UNHEALTHY,
                response_time=0.0,
                timestamp=time.time(),
                details={},
                error_message=str(result)
            )
            for service_name, result in zip(service_names, results)
        }
    
    def get_service_status(self, service_name: str) -> HealthStatus:
        """
        Get current status of a service based on recent checks
        
        Args:
            service_name: Name of the service
            
        Returns:
            Current health status
        """
        if service_name not in self._results or not self._results[service_name]:
            return HealthStatus.UNKNOWN
        
        config = self._configs[service_name]
        recent_results = self._results[service_name][-config.failure_threshold:]
        
        # Count recent failures
        failures = sum(1 for result in recent_results if result.status == HealthStatus.UNHEALTHY)
        
        if failures >= config.failure_threshold:
            return HealthStatus.UNHEALTHY
        elif failures > 0:
            return HealthStatus.DEGRADED
        else:
            return HealthStatus.HEALTHY
    
    def get_all_statuses(self) -> Dict[str, HealthStatus]:
        """Get status of all services"""
        return {
            service_name: self.get_service_status(service_name)
            for service_name in self._checks.keys()
        }
    
    def get_service_history(self, service_name: str, limit: int = 10) -> List[HealthCheckResult]:
        """
        Get recent health check history for a service
        
        Args:
            service_name: Name of the service
            limit: Maximum number of results to return
            
        Returns:
            List of recent health check results
        """
        if service_name not in self._results:
            return []
        
        return self._results[service_name][-limit:]
    
    def get_overall_health(self) -> Dict[str, Any]:
        """
        Get overall system health summary
        
        Returns:
            Health summary
        """
        all_statuses = self.get_all_statuses()
        
        if not all_statuses:
            return {
                'status': HealthStatus.UNKNOWN.value,
                'services': {},
                'summary': {
                    'total': 0,
                    'healthy': 0,
                    'degraded': 0,
                    'unhealthy': 0,
                    'unknown': 0
                }
            }
        
        # Count statuses
        summary = {
            'total': len(all_statuses),
            'healthy': 0,
            'degraded': 0,
            'unhealthy': 0,
            'unknown': 0
        }
        
        for status in all_statuses.values():
            summary[status.value] += 1
        
        # Determine overall status
        if summary['unhealthy'] > 0:
            overall_status = HealthStatus.UNHEALTHY
        elif summary['degraded'] > 0:
            overall_status = HealthStatus.DEGRADED
        elif summary['healthy'] == summary['total']:
            overall_status = HealthStatus.HEALTHY
        else:
            overall_status = HealthStatus.UNKNOWN
        
        return {
            'status': overall_status.value,
            'services': {name: status.value for name, status in all_statuses.items()},
            'summary': summary
        }
    
    async def start_monitoring(self):
        """Start continuous health monitoring"""
        if self._running:
            return
        
        self._running = True
        logger.info("Starting health monitoring")
        
        # Create monitoring tasks for each service
        for service_name in self._checks.keys():
            task = asyncio.create_task(self._monitor_service(service_name))
            self._tasks.append(task)
    
    async def stop_monitoring(self):
        """Stop continuous health monitoring"""
        if not self._running:
            return
        
        self._running = False
        logger.info("Stopping health monitoring")
        
        # Cancel all monitoring tasks
        for task in self._tasks:
            task.cancel()
        
        # Wait for tasks to complete
        if self._tasks:
            await asyncio.gather(*self._tasks, return_exceptions=True)
        
        self._tasks.clear()
    
    async def _monitor_service(self, service_name: str):
        """
        Continuously monitor a service
        
        Args:
            service_name: Name of the service to monitor
        """
        config = self._configs[service_name]
        
        while self._running:
            try:
                if config.enabled:
                    await self.check_service(service_name)
                
                await asyncio.sleep(config.interval)
                
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"Error monitoring service {service_name}: {e}")
                await asyncio.sleep(config.interval)
    
    def enable_service(self, service_name: str):
        """Enable health checks for a service"""
        if service_name in self._configs:
            self._configs[service_name].enabled = True
    
    def disable_service(self, service_name: str):
        """Disable health checks for a service"""
        if service_name in self._configs:
            self._configs[service_name].enabled = False


# Common health check functions
async def http_health_check(url: str, expected_status: int = 200) -> Dict[str, Any]:
    """
    HTTP health check
    
    Args:
        url: URL to check
        expected_status: Expected HTTP status code
        
    Returns:
        Health check result
    """
    import aiohttp
    
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=aiohttp.ClientTimeout(total=5)) as response:
                if response.status == expected_status:
                    return {
                        'status': 'healthy',
                        'details': {
                            'status_code': response.status,
                            'url': url
                        }
                    }
                else:
                    return {
                        'status': 'unhealthy',
                        'details': {
                            'status_code': response.status,
                            'url': url
                        },
                        'error': f"Unexpected status code: {response.status}"
                    }
    except Exception as e:
        return {
            'status': 'unhealthy',
            'details': {'url': url},
            'error': str(e)
        }


async def database_health_check(db_manager) -> Dict[str, Any]:
    """
    Database health check
    
    Args:
        db_manager: Database manager instance
        
    Returns:
        Health check result
    """
    try:
        result = await db_manager.health_check()
        return {
            'status': result.get('status', 'unknown'),
            'details': result
        }
    except Exception as e:
        return {
            'status': 'unhealthy',
            'details': {},
            'error': str(e)
        }