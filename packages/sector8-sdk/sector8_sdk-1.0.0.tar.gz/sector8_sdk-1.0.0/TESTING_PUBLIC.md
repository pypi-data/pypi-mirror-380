# Sector8 SDK Testing Guide

This document provides guidance for testing the Sector8 Python SDK in your development environment.

## Quick Start

### 1. Install Dependencies

```bash
pip install sector8-sdk
pip install pytest pytest-asyncio  # For testing
```

### 2. Basic Configuration

Create a `.env` file with your configuration:

```bash
# Your Sector8 API Key
SECTOR8_API_KEY=your-api-key-here

# Optional: Custom API endpoint
SECTOR8_BASE_URL=https://api.sector8.ai

# Optional: Client identifier
SECTOR8_CLIENT_ID=your-client-id
```

### 3. Run Basic Tests

```bash
# Test installation
python -c "from sector8 import Sector8SimpleClient; print('✓ Import successful')"

# Test basic functionality
python -c "
from sector8 import Sector8SimpleClient
client = Sector8SimpleClient(api_key='test-key')
print('✓ Client initialization successful')
"
```

## Testing Strategy

The SDK supports multiple testing approaches:

1. **Unit Tests** - Fast, isolated testing with mocks
2. **Integration Tests** - End-to-end testing with real API endpoints
3. **Manual Testing** - Interactive testing in your development environment

### Unit Testing with Mocks

```python
import pytest
from unittest.mock import patch
from sector8 import Sector8SimpleClient

def test_client_initialization():
    client = Sector8SimpleClient(api_key="test-key")
    assert client.api_key == "test-key"

@patch('sector8.simple_client.aiohttp.ClientSession.post')
def test_log_llm_call(mock_post):
    mock_post.return_value.json.return_value = {'status': 'success'}
    client = Sector8SimpleClient(api_key="test-key")
    result = client.log_llm_call("openai", "gpt-4", tokens=100, cost=0.002)
    assert result == {'status': 'success'}
```

### Integration Testing

For integration tests, ensure you have:

1. Valid Sector8 API credentials
2. Network access to the API endpoints
3. Proper environment configuration

```python
import asyncio
from sector8 import Sector8SimpleClient

async def test_integration():
    client = Sector8SimpleClient(api_key="your-real-api-key")
    await client.initialize()

    try:
        # Test telemetry logging
        result = await client.save_telemetry(
            provider="openai",
            model="gpt-4",
            prompt="test prompt",
            completion="test completion",
            tokens_used=10,
            latency_ms=100,
            cost=0.001
        )
        print(f"✓ Telemetry logged: {result}")

    finally:
        await client.close()

# Run the test
asyncio.run(test_integration())
```

## Environment Configuration

### Required Environment Variables

```bash
# Sector8 Configuration
SECTOR8_API_KEY=your-api-key
SECTOR8_BASE_URL=https://api.sector8.ai  # Optional
SECTOR8_CLIENT_ID=your-client-id         # Optional

# Testing Configuration
SECTOR8_MOCK_EXTERNAL_APIS=true          # For unit tests
SECTOR8_LOG_LEVEL=INFO                   # Optional
SECTOR8_TIMEOUT=30                       # Optional
```

### API Key Formats

The SDK accepts several API key formats:

- Production keys: `sk-...`
- Test keys: `test-...`
- Development keys: `dev-...`

## Common Testing Scenarios

### 1. Basic Client Operations

```python
from sector8 import Sector8SimpleClient

# Initialize client
client = Sector8SimpleClient(api_key="your-api-key")

# Log LLM usage
client.log_llm_call("openai", "gpt-4", 150, 0.003)

# Alert security threats
client.alert_threat("prompt_injection", "high", "Suspicious input detected")

# Log incidents
client.log_incident("Rate limit exceeded", "medium", tokens=100)
```

### 2. Async Operations

```python
import asyncio
from sector8 import Sector8SimpleClient

async def async_example():
    client = Sector8SimpleClient(api_key="your-api-key")
    await client.initialize()

    # Save telemetry data
    await client.save_telemetry(
        provider="anthropic",
        model="claude-3",
        prompt="Hello",
        completion="Hi there!",
        tokens_used=5,
        latency_ms=200,
        cost=0.0001
    )

    await client.close()

asyncio.run(async_example())
```

### 3. Error Handling

```python
from sector8 import Sector8SimpleClient, ConfigurationError

try:
    # This will raise ConfigurationError
    client = Sector8SimpleClient(api_key="")
except ConfigurationError as e:
    print(f"Configuration error: {e}")

try:
    # This will handle network errors gracefully
    client = Sector8SimpleClient(api_key="test-key")
    client.log_llm_call("openai", "gpt-4", 100, 0.002)
except Exception as e:
    print(f"Operation failed: {e}")
```

## Performance Testing

### Concurrent Requests

```python
import asyncio
from sector8 import Sector8SimpleClient

async def concurrent_test():
    client = Sector8SimpleClient(api_key="your-api-key")
    await client.initialize()

    async def make_request(i):
        return await client.save_telemetry(
            provider="test",
            model=f"model-{i}",
            prompt=f"prompt {i}",
            completion=f"completion {i}",
            tokens_used=10,
            latency_ms=100,
            cost=0.001
        )

    # Test 10 concurrent requests
    tasks = [make_request(i) for i in range(10)]
    results = await asyncio.gather(*tasks)

    await client.close()
    print(f"Completed {len(results)} concurrent requests")

asyncio.run(concurrent_test())
```

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Ensure SDK is installed
   pip install sector8-sdk

   # Verify installation
   python -c "import sector8; print('OK')"
   ```

2. **Authentication Errors**
   ```bash
   # Check API key format
   # Verify environment variables
   # Test with a simple request
   ```

3. **Network Errors**
   ```bash
   # Check internet connectivity
   # Verify firewall settings
   # Test API endpoint accessibility
   ```

### Debug Mode

Enable debug mode for detailed logging:

```python
client = Sector8SimpleClient(api_key="your-api-key", debug=True)
```

Or set environment variable:
```bash
export SECTOR8_DEBUG=true
```

## Best Practices

1. **Use environment variables** for sensitive configuration
2. **Mock external APIs** in unit tests
3. **Test error conditions** explicitly
4. **Use async/await** for better performance
5. **Clean up resources** with proper client closing
6. **Monitor API quotas** and rate limits

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Test Sector8 SDK

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.9'

      - name: Install dependencies
        run: |
          pip install sector8-sdk pytest pytest-asyncio

      - name: Run tests
        env:
          SECTOR8_API_KEY: ${{ secrets.SECTOR8_API_KEY }}
          SECTOR8_MOCK_EXTERNAL_APIS: true
        run: |
          pytest tests/
```

## Support

For testing issues or questions:

1. Check the [documentation](https://docs.sector8.ai)
2. Review [examples](https://github.com/sector8-labs/examples)
3. Contact support: support@sector8.ai

---

**Note**: This guide covers public testing approaches. For advanced testing scenarios or enterprise deployments, consult the full documentation or contact support.