"""
Audit Logger for security events and compliance tracking
"""

import json
import time
import hashlib
from typing import Dict, Any, Optional, List
from datetime import datetime
from enum import Enum
from dataclasses import dataclass, asdict
import logging

logger = logging.getLogger(__name__)


class EventType(Enum):
    """Audit event types"""
    PII_DETECTION = "pii_detection"
    PII_SCRUBBING = "pii_scrubbing"
    API_KEY_ACCESS = "api_key_access"
    API_KEY_ROTATION = "api_key_rotation"
    RATE_LIMIT_EXCEEDED = "rate_limit_exceeded"
    CONFIG_ACCESS = "config_access"
    CONFIG_CHANGE = "config_change"
    AUTHENTICATION = "authentication"
    AUTHORIZATION = "authorization"
    DATA_ACCESS = "data_access"
    ERROR = "error"
    SECURITY_VIOLATION = "security_violation"


class Severity(Enum):
    """Event severity levels"""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class AuditEvent:
    """Audit event structure"""
    event_type: EventType
    severity: Severity
    timestamp: str
    user_id: Optional[str]
    session_id: Optional[str]
    source_ip: Optional[str]
    component: str
    action: str
    resource: Optional[str]
    details: Dict[str, Any]
    success: bool
    error_message: Optional[str] = None
    event_id: Optional[str] = None
    
    def __post_init__(self):
        if self.event_id is None:
            # Generate unique event ID
            event_data = f"{self.timestamp}{self.component}{self.action}{self.user_id}"
            self.event_id = hashlib.sha256(event_data.encode()).hexdigest()[:16]


class AuditLogger:
    """Audit logger for security events and compliance"""
    
    def __init__(self, 
                 log_file: Optional[str] = None,
                 enable_console: bool = True,
                 enable_structured: bool = True,
                 retention_days: int = 90):
        """
        Initialize audit logger
        
        Args:
            log_file: Path to audit log file
            enable_console: Whether to log to console
            enable_structured: Whether to use structured JSON logging
            retention_days: Number of days to retain audit logs
        """
        self.log_file = log_file
        self.enable_console = enable_console
        self.enable_structured = enable_structured
        self.retention_days = retention_days
        self._events = []  # In-memory event buffer
        self._setup_logging()
    
    def _setup_logging(self):
        """Setup logging configuration"""
        self.audit_logger = logging.getLogger('ai_catalyst.audit')
        self.audit_logger.setLevel(logging.INFO)
        
        # Remove existing handlers
        for handler in self.audit_logger.handlers[:]:
            self.audit_logger.removeHandler(handler)
        
        # File handler
        if self.log_file:
            file_handler = logging.FileHandler(self.log_file)
            if self.enable_structured:
                file_handler.setFormatter(logging.Formatter('%(message)s'))
            else:
                file_handler.setFormatter(
                    logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
                )
            self.audit_logger.addHandler(file_handler)
        
        # Console handler
        if self.enable_console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(
                logging.Formatter('AUDIT: %(asctime)s - %(message)s')
            )
            self.audit_logger.addHandler(console_handler)
    
    def log_event(self, event: AuditEvent):
        """
        Log an audit event
        
        Args:
            event: Audit event to log
        """
        # Add to in-memory buffer
        self._events.append(event)
        
        # Log to configured outputs
        if self.enable_structured:
            # Convert event to dict and handle enum serialization
            event_dict = asdict(event)
            event_dict['event_type'] = event.event_type.value
            event_dict['severity'] = event.severity.value
            log_message = json.dumps(event_dict)
        else:
            log_message = (
                f"[{event.event_type.value}] {event.component}.{event.action} "
                f"by {event.user_id or 'system'} - "
                f"{'SUCCESS' if event.success else 'FAILED'}"
            )
            if event.error_message:
                log_message += f" - {event.error_message}"
        
        # Choose log level based on severity
        if event.severity == Severity.CRITICAL:
            self.audit_logger.critical(log_message)
        elif event.severity == Severity.HIGH:
            self.audit_logger.error(log_message)
        elif event.severity == Severity.MEDIUM:
            self.audit_logger.warning(log_message)
        else:
            self.audit_logger.info(log_message)
    
    def log_pii_detection(self, 
                         text_hash: str,
                         pii_types: List[str],
                         user_id: Optional[str] = None,
                         session_id: Optional[str] = None,
                         source_ip: Optional[str] = None):
        """Log PII detection event"""
        event = AuditEvent(
            event_type=EventType.PII_DETECTION,
            severity=Severity.MEDIUM,
            timestamp=datetime.now().isoformat(),
            user_id=user_id,
            session_id=session_id,
            source_ip=source_ip,
            component="pii_processor",
            action="detect",
            resource=text_hash,
            details={
                "pii_types": pii_types,
                "pii_count": len(pii_types)
            },
            success=True
        )
        self.log_event(event)
    
    def log_pii_scrubbing(self,
                         text_hash: str,
                         strategy: str,
                         scrubbed_count: int,
                         user_id: Optional[str] = None,
                         session_id: Optional[str] = None,
                         source_ip: Optional[str] = None,
                         success: bool = True,
                         error_message: Optional[str] = None):
        """Log PII scrubbing event"""
        event = AuditEvent(
            event_type=EventType.PII_SCRUBBING,
            severity=Severity.HIGH,  # High because PII is being processed
            timestamp=datetime.now().isoformat(),
            user_id=user_id,
            session_id=session_id,
            source_ip=source_ip,
            component="pii_processor",
            action="scrub",
            resource=text_hash,
            details={
                "strategy": strategy,
                "scrubbed_count": scrubbed_count
            },
            success=success,
            error_message=error_message
        )
        self.log_event(event)
    
    def log_api_key_access(self,
                          provider: str,
                          user_id: Optional[str] = None,
                          session_id: Optional[str] = None,
                          source_ip: Optional[str] = None,
                          success: bool = True,
                          error_message: Optional[str] = None):
        """Log API key access event"""
        event = AuditEvent(
            event_type=EventType.API_KEY_ACCESS,
            severity=Severity.MEDIUM,
            timestamp=datetime.now().isoformat(),
            user_id=user_id,
            session_id=session_id,
            source_ip=source_ip,
            component="key_vault",
            action="access",
            resource=provider,
            details={"provider": provider},
            success=success,
            error_message=error_message
        )
        self.log_event(event)
    
    def log_api_key_rotation(self,
                           provider: str,
                           user_id: Optional[str] = None,
                           session_id: Optional[str] = None,
                           source_ip: Optional[str] = None,
                           success: bool = True,
                           error_message: Optional[str] = None):
        """Log API key rotation event"""
        event = AuditEvent(
            event_type=EventType.API_KEY_ROTATION,
            severity=Severity.HIGH,
            timestamp=datetime.now().isoformat(),
            user_id=user_id,
            session_id=session_id,
            source_ip=source_ip,
            component="key_vault",
            action="rotate",
            resource=provider,
            details={"provider": provider},
            success=success,
            error_message=error_message
        )
        self.log_event(event)
    
    def log_rate_limit_exceeded(self,
                              identifier: str,
                              limit_type: str,
                              retry_after: float,
                              user_id: Optional[str] = None,
                              session_id: Optional[str] = None,
                              source_ip: Optional[str] = None):
        """Log rate limit exceeded event"""
        event = AuditEvent(
            event_type=EventType.RATE_LIMIT_EXCEEDED,
            severity=Severity.MEDIUM,
            timestamp=datetime.now().isoformat(),
            user_id=user_id,
            session_id=session_id,
            source_ip=source_ip,
            component="rate_limiter",
            action="limit_exceeded",
            resource=identifier,
            details={
                "identifier": identifier,
                "limit_type": limit_type,
                "retry_after": retry_after
            },
            success=False
        )
        self.log_event(event)
    
    def log_config_access(self,
                         config_key: str,
                         is_sensitive: bool,
                         user_id: Optional[str] = None,
                         session_id: Optional[str] = None,
                         source_ip: Optional[str] = None,
                         success: bool = True,
                         error_message: Optional[str] = None):
        """Log configuration access event"""
        severity = Severity.HIGH if is_sensitive else Severity.LOW
        
        event = AuditEvent(
            event_type=EventType.CONFIG_ACCESS,
            severity=severity,
            timestamp=datetime.now().isoformat(),
            user_id=user_id,
            session_id=session_id,
            source_ip=source_ip,
            component="config_manager",
            action="access",
            resource=config_key,
            details={
                "config_key": config_key,
                "is_sensitive": is_sensitive
            },
            success=success,
            error_message=error_message
        )
        self.log_event(event)
    
    def log_security_violation(self,
                             violation_type: str,
                             description: str,
                             user_id: Optional[str] = None,
                             session_id: Optional[str] = None,
                             source_ip: Optional[str] = None,
                             details: Optional[Dict[str, Any]] = None):
        """Log security violation event"""
        event = AuditEvent(
            event_type=EventType.SECURITY_VIOLATION,
            severity=Severity.CRITICAL,
            timestamp=datetime.now().isoformat(),
            user_id=user_id,
            session_id=session_id,
            source_ip=source_ip,
            component="security",
            action="violation",
            resource=violation_type,
            details={
                "violation_type": violation_type,
                "description": description,
                **(details or {})
            },
            success=False
        )
        self.log_event(event)
    
    def get_events(self, 
                   event_type: Optional[EventType] = None,
                   severity: Optional[Severity] = None,
                   component: Optional[str] = None,
                   user_id: Optional[str] = None,
                   start_time: Optional[datetime] = None,
                   end_time: Optional[datetime] = None,
                   limit: int = 100) -> List[AuditEvent]:
        """
        Query audit events with filters
        
        Args:
            event_type: Filter by event type
            severity: Filter by severity
            component: Filter by component
            user_id: Filter by user ID
            start_time: Filter by start time
            end_time: Filter by end time
            limit: Maximum number of events to return
            
        Returns:
            List of matching audit events
        """
        filtered_events = []
        
        for event in self._events:
            # Apply filters
            if event_type and event.event_type != event_type:
                continue
            if severity and event.severity != severity:
                continue
            if component and event.component != component:
                continue
            if user_id and event.user_id != user_id:
                continue
            
            # Time filters
            event_time = datetime.fromisoformat(event.timestamp)
            if start_time and event_time < start_time:
                continue
            if end_time and event_time > end_time:
                continue
            
            filtered_events.append(event)
            
            if len(filtered_events) >= limit:
                break
        
        return filtered_events
    
    def get_security_summary(self, hours: int = 24) -> Dict[str, Any]:
        """
        Get security summary for the last N hours
        
        Args:
            hours: Number of hours to analyze
            
        Returns:
            Security summary statistics
        """
        cutoff_time = datetime.now().timestamp() - (hours * 3600)
        
        recent_events = [
            event for event in self._events
            if datetime.fromisoformat(event.timestamp).timestamp() > cutoff_time
        ]
        
        summary = {
            'total_events': len(recent_events),
            'by_severity': {},
            'by_type': {},
            'by_component': {},
            'failed_events': 0,
            'security_violations': 0,
            'pii_operations': 0,
            'api_key_operations': 0
        }
        
        for event in recent_events:
            # Count by severity
            severity_key = event.severity.value
            summary['by_severity'][severity_key] = summary['by_severity'].get(severity_key, 0) + 1
            
            # Count by type
            type_key = event.event_type.value
            summary['by_type'][type_key] = summary['by_type'].get(type_key, 0) + 1
            
            # Count by component
            component_key = event.component
            summary['by_component'][component_key] = summary['by_component'].get(component_key, 0) + 1
            
            # Special counters
            if not event.success:
                summary['failed_events'] += 1
            
            if event.event_type == EventType.SECURITY_VIOLATION:
                summary['security_violations'] += 1
            
            if event.event_type in [EventType.PII_DETECTION, EventType.PII_SCRUBBING]:
                summary['pii_operations'] += 1
            
            if event.event_type in [EventType.API_KEY_ACCESS, EventType.API_KEY_ROTATION]:
                summary['api_key_operations'] += 1
        
        return summary
    
    def export_events(self, 
                     start_time: Optional[datetime] = None,
                     end_time: Optional[datetime] = None) -> str:
        """
        Export events as JSON
        
        Args:
            start_time: Start time filter
            end_time: End time filter
            
        Returns:
            JSON string of events
        """
        events_to_export = self.get_events(
            start_time=start_time,
            end_time=end_time,
            limit=10000  # Large limit for export
        )
        
        # Convert events to dicts with enum values
        events_data = []
        for event in events_to_export:
            event_dict = asdict(event)
            event_dict['event_type'] = event.event_type.value
            event_dict['severity'] = event.severity.value
            events_data.append(event_dict)
        
        return json.dumps(events_data, indent=2)
    
    def cleanup_old_events(self):
        """Remove events older than retention period"""
        cutoff_time = datetime.now().timestamp() - (self.retention_days * 24 * 3600)
        
        original_count = len(self._events)
        self._events = [
            event for event in self._events
            if datetime.fromisoformat(event.timestamp).timestamp() > cutoff_time
        ]
        
        removed_count = original_count - len(self._events)
        if removed_count > 0:
            logger.info(f"Cleaned up {removed_count} old audit events")
    
    @staticmethod
    def hash_sensitive_data(data: str) -> str:
        """Create hash of sensitive data for audit logging"""
        return hashlib.sha256(data.encode()).hexdigest()[:16]