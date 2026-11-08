def greet(name: str) -> str:
    """Retrun a friendly greeting for the given name."""
    return f"Hello, {name}!"


def add(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    """Return the difference between two integers."""
    return a - b


def is_valid_name(name: str) -> bool:
    """Validate that a name contains meaningful text."""
    return isinstance(name, str) and len(name.strip()) >= 2
