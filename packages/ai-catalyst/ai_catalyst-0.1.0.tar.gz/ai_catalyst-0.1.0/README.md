# AI_Catalyst Framework

[![PyPI version](https://badge.fury.io/py/ai-catalyst.svg)](https://badge.fury.io/py/ai-catalyst)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A production-ready AI components framework with enterprise-grade security, resilience, and async performance optimizations.

## 🚀 Features

### Core Components
- **🤖 Three-Tier LLM System** - Local/Network/OpenAI with concurrent failover (3x faster)
- **🔒 PII Detection & Scrubbing** - Enterprise-grade data protection with audit logging
- **📁 Multi-Format File Processing** - Async streaming for JSON, JSONL, CSV, TXT
- **🗄️ Database Patterns** - Async PostgreSQL with connection pooling
- **⚙️ Configuration Management** - Encrypted config with key rotation
- **📊 System Monitoring** - Health checks and performance metrics

### Security & Resilience
- **🔐 Secure Configuration** - AES-256 encryption for sensitive data
- **🔑 API Key Vault** - Secure storage with automatic rotation
- **🚦 Rate Limiting** - Token bucket algorithm with configurable limits
- **📋 Audit Logging** - Comprehensive compliance tracking
- **🔄 Retry Logic** - Exponential backoff with circuit breakers
- **💚 Health Monitoring** - Continuous service availability checks

## 📦 Installation

```bash
pip install ai-catalyst
```

## ⚡ Quick Start

### Basic Usage
```python
import asyncio
from ai_catalyst import LLMProvider, PIIProcessor, FileProcessor

async def main():
    # LLM with automatic failover
    llm = LLMProvider()
    response = await llm.generate_async("Explain quantum computing")
    print(f"Response: {response['content']}")
    
    # PII scrubbing with audit logging
    pii = PIIProcessor()
    clean_text = await pii.scrub_text_async("Call John at 555-1234")
    print(f"Scrubbed: {clean_text}")  # "Call <NAME> at <PHONE>"
    
    # Async file processing
    processor = FileProcessor()
    async for item in processor.process_file_async("data.json"):
        print(f"Processed: {item['data']}")

asyncio.run(main())
```

### Production Setup with Security
```python
from ai_catalyst import (
    LLMProvider, APIKeyVault, RateLimiter, 
    AuditLogger, SecureConfigManager
)

# Setup secure environment
key_vault = APIKeyVault()
key_vault.store_key('openai', 'your-api-key')

rate_limiter = RateLimiter()
audit_logger = AuditLogger(log_file='audit.log')

# Initialize with security components
llm = LLMProvider(
    key_vault=key_vault,
    rate_limiter=rate_limiter,
    audit_logger=audit_logger
)
```

## 🏗️ Architecture

### Async-First Design
- **Non-blocking I/O** - All operations are async by default
- **Concurrent Processing** - Parallel execution with semaphore control
- **Backward Compatibility** - Sync wrappers for existing code
- **Resource Management** - Proper cleanup and session handling

### Security Model
- **Zero-Trust** - All operations are logged and rate-limited
- **Encryption** - Sensitive data encrypted at rest
- **Audit Trail** - Complete compliance logging
- **Access Control** - API key management with rotation

### Resilience Patterns
- **Circuit Breakers** - Automatic failure detection and recovery
- **Retry Logic** - Exponential backoff with jitter
- **Health Checks** - Continuous service monitoring
- **Graceful Degradation** - Fallback strategies for all components

## 📊 Performance

| Operation | Before | After | Improvement |
|-----------|--------|-------|-------------|
| LLM Failover | 45s | 15s | **3x faster** |
| Batch PII Processing | 60s | 12s | **5x faster** |
| File Processing | Blocking | Streaming | **Non-blocking** |
| Rate Limiting | N/A | <1ms | **Sub-millisecond** |

## 🔧 Configuration

### Environment Variables
```bash
# API Keys
export OPENAI_API_KEY="your-openai-key"
export ANTHROPIC_API_KEY="your-anthropic-key"

# Security
export AI_CATALYST_MASTER_KEY="your-encryption-key"
```

### Configuration File
```yaml
# config.yaml
llm:
  timeout: 30
  model: "gpt-4"
  
security:
  rate_limits:
    openai: "paid"  # or "free"
  audit_log: "audit.log"
  
processing:
  batch_size: 100
  max_concurrency: 10
```

## 🧪 Testing

```bash
# Install with dev dependencies
pip install ai-catalyst[dev]

# Run tests
pytest

# Run with coverage
pytest --cov=ai_catalyst
```

## 📚 Documentation

- **[Migration Guide](ASYNC_MIGRATION_GUIDE.md)** - Upgrading to async
- **[Security Guide](docs/security.md)** - Enterprise security setup
- **[Performance Guide](docs/performance.md)** - Optimization tips
- **[API Reference](docs/api.md)** - Complete API documentation

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/ericmedlock/AI_Catalyst/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ericmedlock/AI_Catalyst/discussions)
- **Security**: Report security issues privately to security@example.com