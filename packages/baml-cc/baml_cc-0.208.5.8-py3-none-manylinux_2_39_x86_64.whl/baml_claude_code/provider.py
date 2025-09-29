"""
Claude Code provider implementation for BAML
"""

from typing import Dict, Any, Optional, Callable
from .client import ClaudeCodeClient
from .error import ClaudeCodeError


class ClaudeCodeProvider:
    """BAML provider for Claude Code"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.client = ClaudeCodeClient(**config)
        self.streaming_enabled = config.get("realtime_streaming", False)
    
    
    def create_client(self) -> ClaudeCodeClient:
        """Create a Claude Code client"""
        return self.client
    
    async def generate_with_streaming(
        self,
        prompt: str,
        on_tick: Optional[Callable] = None,
        **kwargs
    ) -> str:
        """Generate with streaming support and optional callbacks"""
        if not self.streaming_enabled:
            return await self.client.generate(prompt, **kwargs)
        
        # Use extended timeout for streaming (20 minutes default)
        timeout_ms = kwargs.get('timeout_ms', 1200000)  # 20 minutes in milliseconds
        
        result_parts = []
        async for event in self.client.generate_streaming(prompt, timeout_ms=timeout_ms, **kwargs):
            # Handle different event types
            if event.get("type") == "content":
                result_parts.append(event.get("content", ""))
            elif event.get("type") == "system":
                # Handle system updates
                if on_tick:
                    on_tick("system_update", event)
            elif event.get("type") == "tool_output":
                # Handle tool output
                if on_tick:
                    on_tick("tool_output", event)
            elif event.get("type") == "raw_output":
                # Handle raw output (progress messages)
                if on_tick:
                    on_tick("progress", event.get("content", ""))
        
        return "".join(result_parts)
    
    async def generate_with_timeout(
        self,
        prompt: str,
        timeout: Optional[int] = None,
        progress_callback: Optional[Callable] = None,
        **kwargs
    ) -> str:
        """Generate with custom timeout and progress tracking"""
        return await self.client.generate_with_timeout(
            prompt, 
            timeout=timeout, 
            progress_callback=progress_callback, 
            **kwargs
        )
    
    def validate_config(self) -> bool:
        """Validate the provider configuration"""
        try:
            # Check if Claude Code CLI is available
            if not self.client.check_availability():
                raise ClaudeCodeError("Claude Code CLI is not available")
            
            # Validate required fields
            if not self.config.get("model"):
                raise ClaudeCodeError("Model is required")
            
            return True
        except Exception as e:
            raise ClaudeCodeError(f"Configuration validation failed: {str(e)}")
    
    def get_supported_features(self) -> Dict[str, bool]:
        """Get supported features"""
        return {
            "subagents": True,
            "hooks": True,
            "slash_commands": True,
            "memory_files": True,
            "realtime_streaming": True,
            "enhanced_metadata": True,
            "custom_auth": True,
            "cloudplan": True,
            "api_key": True,
        }


