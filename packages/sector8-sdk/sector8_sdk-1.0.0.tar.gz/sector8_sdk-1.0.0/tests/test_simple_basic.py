"""
Basic tests for Sector8 Simple Client
"""

import pytest
import os
from unittest.mock import patch
from sector8.simple_client import Sector8SimpleClient
from sector8.errors import ConfigurationError


class TestSector8SimpleClientBasic:
    """Basic test cases for Sector8SimpleClient"""

    def test_client_initialization_with_api_key(self):
        """Test client initialization with API key"""
        client = Sector8SimpleClient(api_key="test-key", client_id="test-client")
        assert client.api_key == "test-key"
        assert client.client_id == "test-client"
        assert client.base_url == "https://api.sector8.ai"
        assert client.debug is False

    def test_client_initialization_with_custom_base_url(self):
        """Test client initialization with custom base URL"""
        client = Sector8SimpleClient(
            api_key="test-key", 
            base_url="https://test.sector8.ai",
            debug=True
        )
        assert client.api_key == "test-key"
        assert client.base_url == "https://test.sector8.ai"
        assert client.debug is True

    def test_client_initialization_missing_api_key(self):
        """Test client initialization fails without API key"""
        with pytest.raises(ConfigurationError):
            Sector8SimpleClient(api_key="")

    def test_client_initialization_invalid_api_key(self):
        """Test client initialization fails with invalid API key"""
        with pytest.raises(ConfigurationError):
            Sector8SimpleClient(api_key="short")

    def test_valid_api_key_formats(self):
        """Test various valid API key formats"""
        # Valid API key formats should not raise errors
        client1 = Sector8SimpleClient(api_key="sk-test123")
        assert client1.api_key == "sk-test123"
        
        client2 = Sector8SimpleClient(api_key="test-key-123-long-enough")
        assert client2.api_key == "test-key-123-long-enough"
        
        client3 = Sector8SimpleClient(api_key="dev-key-for-testing")
        assert client3.api_key == "dev-key-for-testing"

    def test_client_default_values(self):
        """Test client uses correct default values"""
        client = Sector8SimpleClient(api_key="sk-test123")
        assert client.client_id == "1"  # Default client ID
        assert client.base_url == "https://api.sector8.ai"
        assert client.debug is False
        assert client.session is None  # Not initialized yet
        assert client._initialized is False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])