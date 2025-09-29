"""
Sector8 Simple Client - 3-line integration focused on core API endpoints.

This module provides a simplified client that matches the actual production API
endpoints as shown in the Postman collection, optimized for ease of use.
"""

import os
import json
import time
import asyncio
from datetime import datetime
from typing import Dict, Any, Optional, List
import aiohttp
import logging


from .errors import (
    ConfigurationError, 
    NetworkError, 
    AuthenticationError,
    handle_api_error,
    print_startup_diagnostics
)
# Optional monitoring removed - keeping simple for enterprise release

logger = logging.getLogger(__name__)


class Sector8SimpleClient:
    """
    Simplified Sector8 client for true 3-line integration.
    
    Focused on the core production API endpoints:
    - POST /api/v1/telemetry - Save telemetry data
    - POST /api/v1/threat-alerts - Save threat alerts  
    - POST /api/v1/incident-logs - Save incident logs
    - Uses X-API-Key and X-Client-Id headers for authentication
    """
    
    def __init__(
        self, 
        api_key: str,
        base_url: str = None,
        client_id: str = "1",
        debug: bool = False
    ):
        """
        Initialize the simple client.
        
        Args:
            api_key: Your Sector8 API key
            base_url: API base URL (defaults to production)
            client_id: Client ID for multi-tenant isolation (default: "1")
            debug: Enable debug mode for detailed logging
        """
        # Validate API key
        if not api_key:
            from .errors import ConfigurationError
            raise ConfigurationError.missing_api_key()
        
        # Basic API key format validation (allow test keys for development)
        if not api_key.startswith(('sk-', 'test-', 'dev-')) and len(api_key) < 10:
            from .errors import ConfigurationError
            raise ConfigurationError.invalid_api_key(api_key)
        
        self.api_key = api_key
        self.client_id = client_id
        self.base_url = base_url or "https://api.sector8.ai"  # Default production URL
        self.debug = debug
        self.session: Optional[aiohttp.ClientSession] = None
        self._initialized = False
        
        # Initialize session automatically for header-based auth
        if self.debug:
            print(f"Sector8 Simple Client initialized with client_id: {self.client_id}")
    
    async def initialize(self) -> None:
        """Initialize the client session for header-based authentication."""
        if self._initialized:
            return
            
        self.session = aiohttp.ClientSession()
        self._initialized = True
    
    async def _make_request(self, endpoint: str, data: Dict[str, Any], retries: int = 3) -> Dict[str, Any]:
        """Make authenticated request to API endpoint with retry logic."""
        if not self._initialized:
            await self.initialize()
            
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Content-Type": "application/json",
            "X-API-Key": self.api_key,
            "X-Client-Id": self.client_id
        }
        
        last_error = None
        for attempt in range(retries):
            try:
                timeout = aiohttp.ClientTimeout(total=30, connect=10)
                
                async with self.session.post(
                    url, 
                    json=data, 
                    headers=headers, 
                    timeout=timeout
                ) as response:
                    if response.status == 200:
                        return await response.json()
                    elif response.status == 429:  # Rate limited
                        if attempt < retries - 1:
                            wait_time = (2 ** attempt) + 1  # Exponential backoff
                            if self.debug:
                                print(f"Rate limited, retrying in {wait_time}s (attempt {attempt + 1}/{retries})")
                            await asyncio.sleep(wait_time)
                            continue
                    elif response.status in [500, 502, 503, 504]:  # Server errors
                        if attempt < retries - 1:
                            wait_time = (2 ** attempt) + 1
                            if self.debug:
                                print(f"Server error {response.status}, retrying in {wait_time}s (attempt {attempt + 1}/{retries})")
                            await asyncio.sleep(wait_time)
                            continue
                    
                    # Handle non-retryable errors
                    error_text = await response.text()
                    if response.status == 401:
                        raise AuthenticationError(
                            "Invalid API key or client ID",
                            error_code="AUTH_FAILED",
                            solutions=[
                                "Check your API key format",
                                "Verify client_id is correct",
                                "Ensure API key is enabled",
                                "Check if you're using the correct base URL"
                            ]
                        )
                    elif response.status == 403:
                        raise AuthenticationError(
                            "Access forbidden - insufficient permissions",
                            error_code="ACCESS_DENIED",
                            solutions=[
                                "Check API key permissions",
                                "Verify client_id access rights",
                                "Contact support if permissions should be available"
                            ]
                        )
                    else:
                        response.raise_for_status()
                        
            except asyncio.TimeoutError as e:
                last_error = NetworkError(
                    f"Request timed out (attempt {attempt + 1}/{retries})",
                    error_code="TIMEOUT_ERROR",
                    solutions=[
                        "Check your internet connection",
                        "Verify the API endpoint is accessible",
                        "Try with a longer timeout",
                        "Check if there are network restrictions"
                    ],
                    original_error=e
                )
                if attempt < retries - 1:
                    wait_time = (2 ** attempt) + 1
                    if self.debug:
                        print(f"Timeout error, retrying in {wait_time}s (attempt {attempt + 1}/{retries})")
                    await asyncio.sleep(wait_time)
                    continue
                    
            except aiohttp.ClientError as e:
                last_error = NetworkError(
                    f"Network error: {str(e)} (attempt {attempt + 1}/{retries})",
                    error_code="NETWORK_ERROR",
                    solutions=[
                        "Check your internet connection",
                        "Verify the base_url is correct",
                        "Check if there are firewall restrictions",
                        "Try again in a few moments"
                    ],
                    original_error=e
                )
                if attempt < retries - 1:
                    wait_time = (2 ** attempt) + 1
                    if self.debug:
                        print(f"Network error, retrying in {wait_time}s (attempt {attempt + 1}/{retries})")
                    await asyncio.sleep(wait_time)
                    continue
                    
        # If we get here, all retries failed
        if last_error:
            raise last_error
        else:
            raise NetworkError("All retry attempts failed", error_code="MAX_RETRIES_EXCEEDED")
    
    # Core API methods matching production endpoints
    
    async def save_telemetry(
        self,
        provider: str,
        model: str,
        prompt: str,
        completion: str,
        tokens_used: int,
        latency_ms: float,
        cost: float,
        success: bool = True,
        guard_analysis: str = "Allow,Low",
        metadata: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Save telemetry data to /v1/telemetry endpoint.
        
        Args:
            provider: Service provider (e.g., "openai")
            model: Model identifier (e.g., "gpt-4")
            prompt: Input prompt text
            completion: Output completion text
            tokens_used: Number of tokens processed
            latency_ms: Response time in milliseconds
            cost: Request cost
            success: Whether the request was successful
            guard_analysis: Security analysis result
            metadata: Additional metadata
            
        Returns:
            API response
        """
        data = {
            "provider": provider,
            "model": model,
            "prompt": prompt,
            "completion": completion,
            "tokens_used": tokens_used,
            "latency_ms": int(latency_ms),  # Convert float to int
            "cost": cost,
            "success": success,
            "guard_analysis": guard_analysis,
            "metadata": metadata or {}
        }
        return await self._make_request("/api/v1/telemetry", data)
    
    async def save_threat_alert(
        self,
        threat_type: str,
        severity: str,
        status: str,
        description: str,
        metadata: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """
        Save threat alert to /v1/threat-alerts endpoint.
        
        Args:
            threat_type: Type of threat (e.g., "prompt_injection")
            severity: Severity level (e.g., "High", "Medium", "Low")
            status: Alert status (e.g., "active", "resolved", "investigating")
            description: Detailed description
            metadata: Additional metadata as object
            
        Returns:
            API response
        """
        # Ensure status is lowercase to match API expectations
        status = status.lower()
        
        data = {
            "threat_type": threat_type,
            "severity": severity,
            "status": status,
            "description": description,
            "metadata": metadata or {},
            "alert_datetime": datetime.now().isoformat()
        }
        return await self._make_request("/api/v1/threat-alerts", data)
    
    async def save_incident_log(
        self,
        severity: str,
        tool: str,
        classification: str,
        details: str,
        issue: str,
        tokens: int
    ) -> Dict[str, Any]:
        """
        Save incident log to /v1/incident-logs endpoint.
        
        Args:
            severity: Incident severity (e.g., "medium")
            tool: Tool that generated the incident (e.g., "guard_analysis")
            classification: Incident classification (e.g., "pii_detection")
            details: Additional incident details
            issue: Brief issue description
            tokens: Number of tokens processed
            
        Returns:
            API response
        """
        data = {
            "severity": severity,
            "tool": tool,
            "classification": classification,
            "details": {"message": details},  # Convert string to object
            "issue": issue,
            "tokens": tokens
        }
        return await self._make_request("/api/v1/incident-logs", data)
    
    # Convenience methods for common use cases
    
    def log_llm_call(
        self,
        provider: str,
        model: str,
        tokens: int,
        cost: float,
        latency_ms: float = 1500,
        success: bool = True,
        prompt: str = "N/A",
        completion: str = "N/A"
    ) -> None:
        """
        Log an LLM call with automatic async handling and monitoring.
        
        Usage:
            client.log_llm_call("openai", "gpt-4", 150, 0.003)
        """
        # Monitoring simplified for enterprise release
        if self.debug:
            print(f"LLM call recorded: {provider}/{model} - {tokens} tokens, ${cost:.4f}")
        
        # Handle async call in background
        try:
            loop = asyncio.get_event_loop()
            if not loop.is_running():
                loop.run_until_complete(
                    self.save_telemetry(
                        provider=provider,
                        model=model,
                        prompt=prompt,
                        completion=completion,
                        tokens_used=tokens,
                        latency_ms=latency_ms,
                        cost=cost,
                        success=success
                    )
                )
            else:
                asyncio.create_task(
                    self.save_telemetry(
                        provider=provider,
                        model=model,
                        prompt=prompt,
                        completion=completion,
                        tokens_used=tokens,
                        latency_ms=latency_ms,
                        cost=cost,
                        success=success
                    )
                )
        except Exception as e:
            logger.warning(f"Failed to log LLM call: {e}")
    
    def alert_threat(
        self,
        threat_type: str,
        severity: str = "High",
        description: str = None
    ) -> None:
        """
        Alert a security threat with automatic async handling.
        
        Usage:
            client.alert_threat("prompt_injection", "High", "Suspicious input detected")
        """
        description = description or f"{threat_type.replace('_', ' ').title()} detected"
        
        try:
            loop = asyncio.get_event_loop()
            if not loop.is_running():
                loop.run_until_complete(
                    self.save_threat_alert(
                        threat_type=threat_type,
                        severity=severity,
                        status="active",
                        description=description
                    )
                )
            else:
                asyncio.create_task(
                    self.save_threat_alert(
                        threat_type=threat_type,
                        severity=severity,
                        status="active",
                        description=description
                    )
                )
        except Exception as e:
            logger.warning(f"Failed to alert threat: {e}")
    
    def log_incident(
        self,
        issue: str,
        severity: str = "medium",
        tool: str = "guard_analysis",
        classification: str = "general",
        tokens: int = 0
    ) -> None:
        """
        Log an incident with automatic async handling.
        
        Usage:
            client.log_incident("PII detected in response", "high", tokens=150)
        """
        try:
            loop = asyncio.get_event_loop()
            if not loop.is_running():
                loop.run_until_complete(
                    self.save_incident_log(
                        severity=severity,
                        tool=tool,
                        classification=classification,
                        details=f"Incident logged at {datetime.now().isoformat()}",
                        issue=issue,
                        tokens=tokens
                    )
                )
            else:
                asyncio.create_task(
                    self.save_incident_log(
                        severity=severity,
                        tool=tool,
                        classification=classification,
                        details=f"Incident logged at {datetime.now().isoformat()}",
                        issue=issue,
                        tokens=tokens
                    )
                )
        except Exception as e:
            logger.warning(f"Failed to log incident: {e}")
    
    async def close(self) -> None:
        """Clean up resources."""
        if self.session and not self.session.closed:
            await self.session.close()
    
    def __del__(self):
        """Cleanup on deletion."""
        if hasattr(self, 'session') and self.session and not self.session.closed:
            try:
                loop = asyncio.get_event_loop()
                if not loop.is_running():
                    loop.run_until_complete(self.close())
            except:
                pass  # Ignore cleanup errors