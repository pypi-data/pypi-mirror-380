class UTCPAdapterError(Exception):
    """Base exception for all adapter-related errors."""


class InitializationError(UTCPAdapterError):
    """Raised when the UTCP client cannot be initialized."""


class ToolExecutionError(UTCPAdapterError):
    """
    Raised when a UTCP tool fails to execute via the adapter.
    This typically wraps an exception from the underlying python-utcp SDK.
    """
