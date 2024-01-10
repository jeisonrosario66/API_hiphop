def msg_exception(method, exc):
    """handled exception message

    Args:
        method (self): self
        exc (exception): exception

    Returns:
        exception message
    """
    return f"Exception found in '{method.__name__}: {exc}'"