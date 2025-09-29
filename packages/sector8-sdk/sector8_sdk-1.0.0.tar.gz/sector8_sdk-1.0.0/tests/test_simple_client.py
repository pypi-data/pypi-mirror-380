"""
Test suite for Sector8 Simple Client
"""

import pytest
import os
from unittest.mock import patch, MagicMock
from sector8.simple_client import Sector8SimpleClient


class TestSector8SimpleClient:
    """Test cases for Sector8SimpleClient"""

    def test_client_initialization_with_api_key(self):
        """Test client initialization with API key"""
        client = Sector8SimpleClient(api_key="test-key", client_id="test-client")
        assert client.api_key == "test-key"
        assert client.client_id == "test-client"

    def test_client_initialization_from_env(self):
        """Test client initialization from environment variables"""
        with patch.dict(os.environ, {
            'SECTOR8_API_KEY': 'env-key',
            'SECTOR8_CLIENT_ID': 'env-client'
        }):
            client = Sector8SimpleClient()
            assert client.api_key == "env-key"
            assert client.client_id == "env-client"

    def test_client_initialization_missing_api_key(self):
        """Test client initialization fails without API key"""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(ValueError, match="API key is required"):
                Sector8SimpleClient()

    @patch('sector8.simple_client.aiohttp.ClientSession.post')
    def test_log_llm_call_success(self, mock_post):
        """Test successful LLM call logging"""
        mock_response = MagicMock()
        mock_response.json.return_value = {'status': 'success'}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        client = Sector8SimpleClient(api_key="test-key")
        result = client.log_llm_call("openai", "gpt-4", tokens=100, cost=0.002)
        
        assert result == {'status': 'success'}
        mock_post.assert_called_once()

    @patch('sector8.simple_client.aiohttp.ClientSession.post')
    def test_alert_threat_success(self, mock_post):
        """Test successful threat alert"""
        mock_response = MagicMock()
        mock_response.json.return_value = {'alert_id': '12345'}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        client = Sector8SimpleClient(api_key="test-key")
        result = client.alert_threat("prompt_injection", severity="high")
        
        assert result == {'alert_id': '12345'}
        mock_post.assert_called_once()

    @patch('sector8.simple_client.aiohttp.ClientSession.post')
    def test_log_incident_success(self, mock_post):
        """Test successful incident logging"""
        mock_response = MagicMock()
        mock_response.json.return_value = {'incident_id': '67890'}
        mock_response.raise_for_status = MagicMock()
        mock_post.return_value = mock_response

        client = Sector8SimpleClient(api_key="test-key")
        result = client.log_incident("Rate limit exceeded", severity="medium")
        
        assert result == {'incident_id': '67890'}
        mock_post.assert_called_once()

    def test_validate_api_key_format(self):
        """Test API key validation"""
        client = Sector8SimpleClient(api_key="test-key")
        
        # Valid API key formats
        assert client._validate_api_key("sk-test123") == True
        assert client._validate_api_key("sector8-key-123") == True
        
        # Invalid API key formats
        assert client._validate_api_key("") == False
        assert client._validate_api_key(None) == False
        assert client._validate_api_key("short") == False


if __name__ == "__main__":
    pytest.main([__file__, "-v"])