# Sector8 SDK

[![PyPI version](https://badge.fury.io/py/sector8-sdk.svg)](https://badge.fury.io/py/sector8-sdk)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Enterprise AI Security, Observability, and Intelligence SDK**

The Sector8 SDK provides comprehensive tools for securing, monitoring, and analyzing AI applications. Built for enterprise developers who need robust security, real-time observability, and intelligent insights for their AI systems.

## 🚀 Features

### 🔒 **AI Security & Guardrails**
- **Prompt Injection Detection**: Advanced detection of prompt injection attempts
- **Content Filtering**: Multi-provider content safety scanning (OpenAI, Anthropic, Google)
- **PII Detection**: Automatic identification of sensitive data
- **Compliance Validation**: Built-in compliance checking for enterprise requirements
- **Security Templates**: Pre-built security templates for common use cases

### 📊 **Observability & Monitoring**
- **Real-time Telemetry**: Comprehensive telemetry collection and analysis
- **Cost Tracking**: Detailed LLM cost monitoring and optimization
- **Performance Metrics**: Latency, throughput, and error rate tracking
- **Multi-tenant Support**: Isolated monitoring per tenant/client
- **OpenTelemetry Integration**: Standards-compliant observability

### 🧠 **AI Intelligence**
- **Provider Management**: Unified interface for multiple LLM providers
- **Auto-discovery**: Automatic detection and configuration of AI providers
- **Health Monitoring**: Real-time provider health and status tracking
- **Usage Analytics**: Detailed insights into AI usage patterns

## 📦 Installation

```bash
pip install sector8
```

### With Optional Dependencies

```bash
# All features
pip install sector8[all]

# Specific integrations
pip install sector8[openai,anthropic,google]
```

## 🚀 Quick Start (3-line setup)

### 1. Environment Setup
Copy `.env.example` to `.env` and add your API key:
```bash
# Copy environment template
cp .env.example .env

# Add your Sector8 API key
export SECTOR8_API_KEY="sk-your-api-key"
```

### 2. Decorator Pattern (Recommended)
```python
import sector8
from openai import AsyncOpenAI

@sector8.track()
async def analyze_text(text: str) -> str:
    client = AsyncOpenAI()
    response = await client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text}]
    )
    return response.choices[0].message.content

# That's it! All calls are automatically tracked
result = await analyze_text("What is AI?")
```

### 3. Manual Setup (Alternative)
```python
import sector8

# Simple 3-line setup
client = sector8.setup(api_key="your-sector8-api-key")
client.log_llm_call("openai", "gpt-4", tokens=150, cost=0.003)
```

**📚 [Full Documentation](https://docs.sector8.ai) • 🎯 [Dashboard](https://dashboard.sector8.ai) • 🔧 [Examples](./examples/)**

### 2. Content Security Scanning

```python
from sector8.guard import guard_registry

# Scan content for security issues
async def scan_content():
    content = "Your content to scan..."
    
    # Use OpenAI guard
    openai_guard = guard_registry.get_provider("openai")
    result = await openai_guard.check_content(content)
    
    if result.is_safe:
        print("✅ Content is safe")
    else:
        print(f"❌ Issues found: {len(result.issues)}")
        for issue in result.issues:
            print(f"  - {issue.message}")

# Run the scan
import asyncio
asyncio.run(scan_content())
```

### 3. Prompt Validation

```python
from sector8.guard import prompt_validator

# Validate a prompt for injection attempts
prompt = "Your prompt here..."
issues = prompt_validator.validate_prompt(prompt)

if not issues:
    print("✅ Prompt is safe")
else:
    print(f"❌ Found {len(issues)} issues:")
    for issue in issues:
        print(f"  - {issue.message} (Severity: {issue.severity.value})")
```

### 4. Telemetry Collection

```python
from sector8.observability import TelemetryCollector

# Initialize telemetry
collector = TelemetryCollector()

# Track an operation
with collector.track_operation("llm_request", {"model": "gpt-4"}):
    # Your LLM operation here
    response = await llm_client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Hello"}]
    )
    
    # Track the response
    collector.record_llm_response(
        model="gpt-4",
        tokens_used=response.usage.total_tokens,
        cost=response.usage.total_tokens * 0.00003  # Example cost calculation
    )
```

## 🛠️ Command Line Interface

The Sector8 SDK includes a comprehensive CLI for testing and management:

```bash
# Test connection to Sector8 API
sector8 test-connection --api-key YOUR_API_KEY

# Scan content for security issues
sector8 scan-content --content "Content to scan" --provider openai

# Validate a prompt
sector8 validate-prompt --prompt "Your prompt here"

# List available guard providers
sector8 list-providers

# Check health status
sector8 health

# Create configuration file
sector8 create-config --output config.json

# Show version information
sector8 version
```

## 🔧 Configuration

### Environment Variables

```bash
# Required
export SECTOR8_API_KEY="your-api-key"

# Optional
export SECTOR8_API_BASE_URL="https://api.sector8.ai"
export SECTOR8_LOG_LEVEL="INFO"
export SECTOR8_TENANT_ID="your-tenant-id"
```

### Configuration File

Create a `config.json` file:

```json
{
  "api_key": "your-api-key",
  "api_base_url": "https://api.sector8.ai",
  "log_level": "INFO",
  "tenant_id": "your-tenant-id",
  "telemetry": {
    "enabled": true,
    "endpoint": "https://telemetry.sector8.ai"
  },
  "guard": {
    "providers": ["openai", "anthropic", "google"],
    "auto_scan": true
  }
}
```

## 🏗️ Architecture

The Sector8 SDK is built with a modular architecture:

```
sector8/
├── core/           # Core SDK functionality
├── guard/          # Security and content filtering
├── observability/  # Telemetry and monitoring
├── instrumentation/ # Auto-instrumentation
├── providers/      # LLM provider integrations
└── cli/           # Command line interface
```

### Key Components

- **Guard System**: Multi-provider content safety and security scanning
- **Telemetry Engine**: Real-time data collection and analysis
- **Provider Registry**: Unified interface for LLM providers
- **Configuration Manager**: Centralized configuration management
- **CLI Tools**: Command-line utilities for testing and management

## 🔌 Provider Integrations

### Supported LLM Providers

- **OpenAI**: GPT-4, GPT-3.5-turbo, and other OpenAI models
- **Anthropic**: Claude models with safety features
- **Google AI**: Gemini models with content filtering
- **Azure OpenAI**: Enterprise OpenAI deployments
- **AWS Bedrock**: Amazon's managed AI service

### Adding Custom Providers

```python
from sector8.guard import GuardProvider, GuardResult

class CustomGuard(GuardProvider):
    async def check_content(self, content: str, context=None) -> GuardResult:
        # Your custom content checking logic
        return GuardResult(
            is_safe=True,
            confidence=0.9,
            issues=[],
            recommendations=["Custom recommendation"]
        )

# Register your custom provider
from sector8.guard import guard_registry
guard_registry.register_provider("custom", CustomGuard())
```

## 📊 Monitoring & Analytics

### Dashboard Integration

The SDK provides seamless integration with the Sector8 dashboard:

```python
# Enable dashboard integration
config = SDKConfig(
    dashboard_enabled=True,
    dashboard_url="https://dashboard.sector8.ai"
)

# Real-time metrics will be automatically sent to your dashboard
```

### Custom Metrics

```python
from sector8.observability import metrics

# Record custom metrics
metrics.counter("custom_operation", 1, {"operation": "data_processing"})
metrics.gauge("memory_usage", 85.5, {"component": "ai_model"})
metrics.histogram("response_time", 0.125, {"endpoint": "/api/chat"})
```

## 🔒 Security

The Sector8 SDK is built with security as a top priority:

### **Security Features**
- ✅ **Zero hardcoded secrets** - All credentials handled securely
- ✅ **HTTPS-only communication** - All external requests use encryption
- ✅ **API key validation** - Required for all operations with schema validation
- ✅ **Multi-tenant isolation** - Complete tenant context management
- ✅ **Input sanitization** - All inputs validated via Pydantic
- ✅ **Audit logging** - Complete security event tracking

### **Security Validation**
- ✅ **Bandit scan**: 0 HIGH/CRITICAL issues
- ✅ **Dependency audit**: All packages scanned for vulnerabilities
- ✅ **Package validation**: Clean metadata and structure
- ✅ **Code review**: Security-focused development practices

### **Secure API Key Handling**
```python
# Never hardcode API keys in your code
import sector8

# Use environment variables or secure configuration
sector8.configure(
    client_id="your-client-id",
    api_key="your-api-key"  # Load from environment or secure config
)
```

For detailed security information, see [Security Checklist](docs/security_checklist.md).

## 🧪 Testing

### Unit Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=sector8 --cov-report=html

# Run specific test categories
pytest -m "not slow"  # Skip slow tests
pytest -m integration  # Only integration tests
```

### Integration Tests

```bash
# Test with real API (requires API key)
export SECTOR8_API_KEY="your-test-api-key"
pytest tests/integration/

# Test SDK import and basic functionality
python -c "import sector8; client = sector8.setup(api_key='test'); print('✅ SDK working')"
```

### Performance Tests

```bash
# Run performance benchmarks
pytest tests/performance/ -v
```

## 📚 Advanced Usage

### Configuration Wizard

```python
import sector8

# Interactive setup wizard
client = sector8.configure_wizard()
# Follow the prompts to configure your SDK
```

### Environment Variables

```bash
export SECTOR8_API_KEY="your-api-key"
export SECTOR8_BASE_URL="https://api.sector8.ai"  # Optional
export SECTOR8_CLIENT_ID="your-client-id"         # Optional
```

### Configuration File

Create a `.sector8rc` file:

```json
{
  "api_key": "your-api-key",
  "base_url": "https://api.sector8.ai",
  "client_id": "your-client-id",
  "debug": false
}
```

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Development Setup

```bash
git clone https://github.com/sector8/sector8-sdk.git
cd sector8-sdk
pip install -e ".[dev]"
pre-commit install
```

### Running Tests

```bash
# Full test suite
make test

# Quick tests
make test-unit

# Security scans
make security-scan
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- 📖 [Documentation](https://docs.sector8.ai)
- 🐛 [Report Issues](https://github.com/sector8/sector8-sdk/issues)
- 💬 [Community Discussion](https://github.com/sector8/sector8-sdk/discussions)
- ✉️ [Email Support](mailto:support@sector8.ai)

---

**Made with ❤️ by the Sector8 team**