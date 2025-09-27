"""
Claude Code client implementation for Python
"""

import asyncio
import subprocess
import json
import os
from typing import Dict, List, Optional, Any, Union, AsyncIterator, Callable
from pathlib import Path

from .error import ClaudeCodeError


class ClaudeCodeClient:
    """Claude Code client for BAML"""
    
    def __init__(
        self,
        model: str = "sonnet",
        api_key: Optional[str] = None,
        claude_binary: Optional[str] = None,
        **kwargs
    ):
        self.model = model
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        self.claude_binary = claude_binary or "claude"
        self.options = kwargs
        
    async def generate_streaming(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        output_format: str = "stream-json",
        include_partial_messages: bool = True,
        **kwargs
    ) -> AsyncIterator[Dict[str, Any]]:
        """Generate a streaming response using Claude Code"""
        try:
            # Build command arguments with streaming options
            args = [self.claude_binary, "code", "--print", "--verbose", "--model", self.model]
            
            if self.api_key:
                args.extend(["--api-key", self.api_key])
            
            # Note: Claude Code CLI doesn't support --max-tokens or --temperature
            # These parameters are handled by the model itself
            
            # Add streaming options
            args.extend(["--output-format", output_format])
            if include_partial_messages:
                args.extend(["--include-partial-messages"])
            
            # Add custom options
            for key, value in kwargs.items():
                if value is not None:
                    args.extend([f"--{key.replace('_', '-')}", str(value)])
            
            # Execute command with streaming, passing prompt via stdin
            process = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                stdin=asyncio.subprocess.PIPE
            )
            
            # Send prompt via stdin
            process.stdin.write(prompt.encode())
            process.stdin.close()
            
            # Stream output line by line
            async for line in process.stdout:
                line = line.decode().strip()
                if line:
                    try:
                        # Parse JSON event
                        event = json.loads(line)
                        yield event
                    except json.JSONDecodeError:
                        # Handle non-JSON output (e.g., progress messages)
                        yield {"type": "raw_output", "content": line}
            
            # Wait for process to complete
            await process.wait()
            
            if process.returncode != 0:
                stderr = await process.stderr.read()
                raise ClaudeCodeError(f"Claude Code execution failed: {stderr.decode()}")
                
        except Exception as e:
            raise ClaudeCodeError(f"Failed to generate streaming response: {str(e)}")

    async def generate(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        streaming: bool = False,
        **kwargs
    ) -> Union[str, AsyncIterator[Dict[str, Any]]]:
        """Generate a response using Claude Code with optional streaming"""
        if streaming:
            return self.generate_streaming(prompt, max_tokens, temperature, **kwargs)
        
        # Original non-streaming implementation
        try:
            # Build command arguments
            args = [self.claude_binary, "code", "--print", "--model", self.model]
            
            if self.api_key:
                args.extend(["--api-key", self.api_key])
            
            # Note: Claude Code CLI doesn't support --max-tokens or --temperature
            # These parameters are handled by the model itself
            
            # Add custom options
            for key, value in kwargs.items():
                if value is not None:
                    args.extend([f"--{key.replace('_', '-')}", str(value)])
            
            # Execute command, passing prompt via stdin
            process = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                stdin=asyncio.subprocess.PIPE
            )
            
            # Send prompt via stdin and wait for completion
            stdout, stderr = await process.communicate(input=prompt.encode())
            
            if process.returncode != 0:
                raise ClaudeCodeError(f"Claude Code execution failed: {stderr.decode()}")
            
            return stdout.decode().strip()
            
        except Exception as e:
            raise ClaudeCodeError(f"Failed to generate response: {str(e)}")
    
    async def generate_with_timeout(
        self,
        prompt: str,
        timeout: Optional[int] = None,
        progress_callback: Optional[Callable] = None,
        **kwargs
    ) -> str:
        """Generate with custom timeout and progress tracking"""
        timeout = timeout or 300  # Default 5 minutes
        
        try:
            if kwargs.get("streaming", False):
                # Use streaming with timeout
                result_parts = []
                stream = self.generate_streaming(prompt, **{k: v for k, v in kwargs.items() if k != "streaming"})
                
                async def process_stream():
                    async for event in stream:
                        if event.get("type") == "content":
                            result_parts.append(event.get("content", ""))
                        elif event.get("type") == "system" and progress_callback:
                            progress_callback("system_update", event)
                        elif event.get("type") == "tool_output" and progress_callback:
                            progress_callback("tool_output", event)
                        elif event.get("type") == "raw_output" and progress_callback:
                            progress_callback("progress", event.get("content", ""))
                
                await asyncio.wait_for(process_stream(), timeout=timeout)
                return "".join(result_parts)
            else:
                # Use regular generate with timeout
                return await asyncio.wait_for(
                    self.generate(prompt, **kwargs),
                    timeout=timeout
                )
        except asyncio.TimeoutError:
            raise ClaudeCodeError(f"Claude Code operation timed out after {timeout} seconds")

    def generate_sync(
        self,
        prompt: str,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
        **kwargs
    ) -> str:
        """Synchronous version of generate"""
        return asyncio.run(self.generate(prompt, max_tokens, temperature, **kwargs))
    
    def check_availability(self) -> bool:
        """Check if Claude Code CLI is available"""
        try:
            result = subprocess.run(
                [self.claude_binary, "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            return result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            return False
    
    def get_version(self) -> Optional[str]:
        """Get Claude Code version"""
        try:
            result = subprocess.run(
                [self.claude_binary, "--version"],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                return result.stdout.strip()
            return None
        except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError):
            return None


