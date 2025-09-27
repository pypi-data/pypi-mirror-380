"""
BAML Claude Code Provider

This package provides a Claude Code provider for BAML, enabling advanced
Claude Code features including subagents, hooks, slash commands, and more.
"""

from .client import ClaudeCodeClient
from .provider import ClaudeCodeProvider
from .error import ClaudeCodeError

__version__ = "1.0.0"
__all__ = ["ClaudeCodeClient", "ClaudeCodeProvider", "ClaudeCodeError"]

# Re-export commonly used types
try:
    from baml_py import LLMClient, LLMClientError
    __all__.extend(["LLMClient", "LLMClientError"])
except ImportError:
    pass


