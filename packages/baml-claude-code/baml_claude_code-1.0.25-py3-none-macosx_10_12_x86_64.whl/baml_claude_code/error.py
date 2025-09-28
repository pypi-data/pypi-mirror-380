"""
Error types for the BAML Claude Code provider
"""


class ClaudeCodeError(Exception):
    """Base exception for Claude Code provider errors"""
    pass


class ClaudeCodeConfigError(ClaudeCodeError):
    """Configuration error"""
    pass


class ClaudeCodeExecutionError(ClaudeCodeError):
    """Execution error"""
    pass


class ClaudeCodeAuthenticationError(ClaudeCodeError):
    """Authentication error"""
    pass


class ClaudeCodeTimeoutError(ClaudeCodeError):
    """Timeout error"""
    pass


