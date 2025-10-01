"""
AI_Catalyst - Reusable AI Components Framework

A collection of proven, reusable components for AI applications including:
- Three-tier LLM providers (local/network/OpenAI) with async support
- PII detection and scrubbing with concurrent processing
- File processing and data handling with streaming support
- Database patterns and configuration management
- System monitoring and performance tuning

Async Methods:
- LLMProvider.generate_async() - Non-blocking LLM generation with concurrent failover
- PIIProcessor.scrub_text_async() - Async PII scrubbing
- PIIProcessor.batch_scrub_texts_async() - Concurrent batch processing
- FileProcessor.process_file_async() - Streaming file processing
- FileProcessor.process_directory_async() - Concurrent directory processing

Sync methods remain available for backward compatibility.
"""

__version__ = "0.1.1"
__author__ = "Eric Medlock"

# Core imports for easy access
from .llm import LLMProvider
from .data.processors import FileProcessor
from .data.pii import PIIProcessor
from .config import ConfigManager
from .database import DatabaseManager

# Security components
from .security import SecureConfigManager, APIKeyVault, RateLimiter, AuditLogger

# Resilience components  
from .resilience import RetryHandler, CircuitBreaker, HealthChecker

__all__ = [
    "LLMProvider",
    "FileProcessor", 
    "PIIProcessor",
    "ConfigManager",
    "DatabaseManager",
    "SecureConfigManager",
    "APIKeyVault",
    "RateLimiter", 
    "AuditLogger",
    "RetryHandler",
    "CircuitBreaker",
    "HealthChecker"
]