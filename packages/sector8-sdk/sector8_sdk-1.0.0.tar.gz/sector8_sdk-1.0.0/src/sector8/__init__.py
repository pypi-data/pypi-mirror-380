"""
Sector8 SDK - Enterprise LLM Observability

A comprehensive SDK for monitoring and observability of Large Language Model applications.
"""

__version__ = "1.0.0"

import os
import functools
import inspect
import time
from typing import Optional, Callable, Any, Dict

from .simple_client import Sector8SimpleClient
from .config_wizard import run_configuration_wizard

# Advanced features removed for enterprise v1.0.0 simplicity
_advanced_features = False

# Instrumentation removed for enterprise v1.0.0 simplicity  
_instrumentation_available = False

# Global client instances
_client = None
_simple_client = None

# DECORATOR PATTERN - Dashboard Integration (Tier 1)
def track(
    provider: str = None,
    model: str = None,
    cost_per_token: float = None,
    auto_detect: bool = True
):
    """
    Decorator for automatic LLM function tracking and telemetry.
    
    Matches the dashboard integration pattern:
    
    @sector8.track()
    async def analyze_text(text: str) -> str:
        client = AsyncOpenAI()
        response = await client.chat.completions.create(...)
        return response.choices[0].message.content
    
    Args:
        provider: LLM provider ('openai', 'anthropic', etc.) - auto-detected if not provided
        model: Model name ('gpt-4', 'claude-3', etc.) - auto-detected if not provided  
        cost_per_token: Custom pricing - calculated automatically if not provided
        auto_detect: Enable automatic detection of provider/model from function calls
        
    Environment Variables:
        SECTOR8_API_KEY: Required - Your Sector8 API key
        OPENAI_API_KEY: Optional - For OpenAI integration
        ANTHROPIC_API_KEY: Optional - For Anthropic integration
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def async_wrapper(*args, **kwargs):
            # Get or initialize the client
            global _simple_client
            if _simple_client is None:
                # Auto-initialize from environment
                api_key = os.getenv('SECTOR8_API_KEY')
                if not api_key:
                    print("Warning: SECTOR8_API_KEY not found. Set environment variable for telemetry.")
                    return await func(*args, **kwargs)  # Run function without tracking
                
                _simple_client = Sector8SimpleClient(api_key=api_key)
            
            # Track function execution
            start_time = time.time()
            function_name = func.__name__
            
            try:
                # Execute the original function
                result = await func(*args, **kwargs)
                end_time = time.time()
                latency_ms = int((end_time - start_time) * 1000)
                
                # Auto-detect provider and model from result/context
                detected_provider = provider or _detect_provider_from_function(func, result)
                detected_model = model or _detect_model_from_function(func, result, args, kwargs)
                
                # Log to Sector8
                _simple_client.log_llm_call(
                    provider=detected_provider or "unknown",
                    model=detected_model or "unknown", 
                    tokens=_estimate_tokens_from_result(result),
                    cost=_estimate_cost_from_result(result, detected_provider, detected_model),
                    latency_ms=latency_ms,
                    prompt=_extract_prompt_from_args(args, kwargs) or "N/A",
                    completion=_extract_completion_from_result(result) or "N/A",
                    success=True
                )
                
                return result
                
            except Exception as e:
                end_time = time.time()
                latency_ms = int((end_time - start_time) * 1000)
                
                # Log failed attempt
                if _simple_client:
                    _simple_client.log_llm_call(
                        provider=provider or "unknown",
                        model=model or "unknown",
                        tokens=0,
                        cost=0.0,
                        latency_ms=latency_ms,
                        success=False,
                        prompt="N/A",
                        completion=f"Error: {str(e)}"
                    )
                
                raise  # Re-raise the original exception
        
        @functools.wraps(func)
        def sync_wrapper(*args, **kwargs):
            # Get or initialize the client
            global _simple_client
            if _simple_client is None:
                api_key = os.getenv('SECTOR8_API_KEY')
                if not api_key:
                    print("Warning: SECTOR8_API_KEY not found. Set environment variable for telemetry.")
                    return func(*args, **kwargs)
                
                _simple_client = Sector8SimpleClient(api_key=api_key)
            
            # Track function execution
            start_time = time.time()
            function_name = func.__name__
            
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                latency_ms = int((end_time - start_time) * 1000)
                
                # Auto-detect and log
                detected_provider = provider or _detect_provider_from_function(func, result)
                detected_model = model or _detect_model_from_function(func, result, args, kwargs)
                
                _simple_client.log_llm_call(
                    provider=detected_provider or "unknown",
                    model=detected_model or "unknown",
                    tokens=_estimate_tokens_from_result(result),
                    cost=_estimate_cost_from_result(result, detected_provider, detected_model),
                    latency_ms=latency_ms,
                    success=True,
                    prompt=_extract_prompt_from_args(args, kwargs) or "N/A",
                    completion=_extract_completion_from_result(result) or "N/A"
                )
                
                return result
                
            except Exception as e:
                end_time = time.time()
                latency_ms = int((end_time - start_time) * 1000)
                
                if _simple_client:
                    _simple_client.log_llm_call(
                        provider=provider or "unknown", 
                        model=model or "unknown",
                        tokens=0,
                        cost=0.0,
                        latency_ms=latency_ms,
                        success=False,
                        prompt="N/A",
                        completion=f"Error: {str(e)}"
                    )
                raise
        
        # Return appropriate wrapper based on function type
        if inspect.iscoroutinefunction(func):
            return async_wrapper
        else:
            return sync_wrapper
    
    return decorator

def _detect_provider_from_function(func, result):
    """Auto-detect LLM provider from function context."""
    func_source = inspect.getsource(func) if hasattr(func, '__code__') else ""
    
    if "openai" in func_source.lower() or "OpenAI" in func_source:
        return "openai"
    elif "anthropic" in func_source.lower() or "claude" in func_source.lower():
        return "anthropic"  
    elif "google" in func_source.lower() or "gemini" in func_source.lower():
        return "google"
    
    return None

def _detect_model_from_function(func, result, args, kwargs):
    """Auto-detect model from function arguments or result."""
    # Check function arguments for model parameter
    for arg in kwargs.values():
        if isinstance(arg, str):
            if "gpt-4" in arg.lower():
                return "gpt-4"
            elif "gpt-3.5" in arg.lower():
                return "gpt-3.5-turbo"
            elif "claude" in arg.lower():
                return "claude-3"
            elif "gemini" in arg.lower():
                return "gemini-pro"
    
    return None

def _estimate_tokens_from_result(result):
    """Estimate token count from result."""
    if isinstance(result, str):
        # Rough estimate: 1 token ≈ 4 characters
        return max(1, len(result) // 4)
    return 1

def _estimate_cost_from_result(result, provider, model):
    """Estimate cost from result."""
    tokens = _estimate_tokens_from_result(result)
    
    # Basic cost estimation (these would be more accurate in production)
    cost_per_1k = {
        ("openai", "gpt-4"): 0.03,
        ("openai", "gpt-3.5-turbo"): 0.002,
        ("anthropic", "claude-3"): 0.015,
        ("google", "gemini-pro"): 0.001,
    }
    
    rate = cost_per_1k.get((provider, model), 0.001)
    return (tokens / 1000) * rate

def _extract_prompt_from_args(args, kwargs):
    """Extract prompt from function arguments."""
    # Look for common prompt parameter names
    for key in ['text', 'prompt', 'message', 'content', 'input']:
        if key in kwargs and isinstance(kwargs[key], str):
            return kwargs[key][:500]  # Limit length
    
    # Check positional args for strings
    for arg in args:
        if isinstance(arg, str) and len(arg) > 10:
            return arg[:500]
    
    return None

def _extract_completion_from_result(result):
    """Extract completion from function result."""
    if isinstance(result, str):
        return result[:1000]  # Limit length
    return None

# 3-LINE INTEGRATION - Primary API (Tier 2)
def setup(api_key: str = None, debug: bool = False, **kwargs) -> Sector8SimpleClient:
    """
    Quick 3-line setup for Sector8 monitoring.
    
    Usage:
        import sector8
        client = sector8.setup(api_key="your-key")
        client.log_llm_call("openai", "gpt-4", tokens=150, cost=0.003)
    
    Args:
        api_key: Your Sector8 API key (or set SECTOR8_API_KEY env var)
        debug: Enable debug output for troubleshooting
        **kwargs: Additional options (base_url, client_id)
    
    Returns:
        Ready-to-use Sector8SimpleClient
    """
    global _simple_client
    
    # Auto-detect from environment
    api_key = api_key or os.getenv('SECTOR8_API_KEY')
    
    if not api_key:
        from .errors import ConfigurationError
        raise ConfigurationError.missing_api_key()
    
    _simple_client = Sector8SimpleClient(api_key=api_key, debug=debug, **kwargs)
    return _simple_client

def get_simple_client() -> Sector8SimpleClient:
    """Get the configured simple client."""
    global _simple_client
    if _simple_client is None:
        raise RuntimeError("Sector8 SDK not initialized. Call sector8.setup() first.")
    return _simple_client

# Configuration wizard for guided setup
def configure_wizard(save_to_file: bool = True) -> Sector8SimpleClient:
    """
    Run interactive configuration wizard for guided setup.
    
    Usage:
        import sector8
        client = sector8.configure_wizard()
    
    Returns:
        Configured Sector8SimpleClient ready to use
    """
    config = run_configuration_wizard(save_to_file=save_to_file)
    
    # Create simple client from wizard configuration
    return setup(
        api_key=config.get('api_key'),
        base_url=config.get('base_url')
    )

# LEGACY/ADVANCED API (backwards compatibility)
def configure(
    client_id: str = None,
    api_key: str = None,
    endpoint: str = None,
    **kwargs
):
    """Configure Sector8 SDK - redirects to simple client for enterprise v1.0.0."""
    print("Advanced SDK features not available in enterprise v1.0.0. Using simple client.")
    return setup(api_key=api_key, base_url=endpoint, client_id=client_id, **kwargs)

def get_client():
    """Get the configured SDK client instance - redirects to simple client."""
    global _simple_client
    if _simple_client is None:
        raise RuntimeError("SDK not configured. Call sector8.setup() first.")
    return _simple_client

def auto_instrument() -> None:
    """Auto-instrumentation not available in enterprise v1.0.0 - use decorator pattern instead."""
    print("Auto-instrumentation not available in enterprise v1.0.0.")
    print("Use @sector8.track() decorator or client.log_llm_call() for monitoring instead.")
    print("Example: @sector8.track() above your LLM functions.")


__all__ = [
    # Enterprise Integration - Primary API for v1.0.0
    "track",  # @sector8.track() decorator
    "setup",  # 3-line integration
    "get_simple_client",
    "configure_wizard",
    
    # Client Classes
    "Sector8SimpleClient", 
    
    # Legacy API (redirects to simple client)
    "configure", 
    "get_client", 
    "auto_instrument",
    "run_configuration_wizard"
]
