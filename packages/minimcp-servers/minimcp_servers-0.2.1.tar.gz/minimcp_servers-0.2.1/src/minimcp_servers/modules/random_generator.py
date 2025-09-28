import secrets
import string
import sys
import uuid


def generate_uuid() -> str:
    """Generate and return a cryptographically secure random UUID string using uuid4"""
    return str(uuid.uuid4())


def generate_random_number(min_value: int = 0, max_value: int = sys.maxsize) -> int:
    f"""
    Generate and return a cryptographically secure random number between min_value and max_value (inclusive).
    Default min_value and max_value are 0 and {sys.maxsize} respectively.
    """
    if min_value >= max_value:
        raise ValueError("min_value must be < max_value")
    return min_value + secrets.randbelow(max_value - min_value + 1)


def generate_random_text(length: int = 10) -> str:
    """
    Generate and return a cryptographically secure text string of the specified length.
    Default length is 10.

    Args:
        length: The length of the string to generate (must be non-negative)

    Returns:
        A random string containing letters and digits

    Raises:
        ValueError: If length is negative
    """
    if length < 0:
        raise ValueError("length must be non-negative")
    if length == 0:
        return ""
    alphabets = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabets) for _ in range(length))
