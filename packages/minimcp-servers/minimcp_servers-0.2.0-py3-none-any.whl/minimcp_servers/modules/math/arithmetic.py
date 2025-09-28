import math as stdlib_math

# Creating a custom module as basic math operations and built-in functions
# are NOT directly provided by the standard math module. Additionally argument types from
# the standard math module are not directly compatible with the MiniMCP protocol.


# === Elementary Functions ===


def add(array: list[float]) -> float:
    """
    Return the sum of all the elements in the array of numbers.
    When the array is empty, return 0.
    """
    return stdlib_math.fsum(array)


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b"""
    return a - b


def multiply(array: list[float]) -> float:
    """
    Return the product of all the elements in the array of numbers.
    When the array is empty, return 1.
    """
    return stdlib_math.prod(array)


def divide(a: float, b: float) -> float:
    """Return the quotient of a and b"""
    return a / b


def modulo(a: float, b: float) -> float:
    """Floor-division modulo: Return the remainder of a divided by b"""
    return a % b


def floor_divide(a: float, b: float) -> float:
    """Return the floor division of a by b"""
    return a // b


def pow(a: float, b: float) -> float:
    """Return a raised to the power of b"""
    return a**b


def minimum(array: list[float]) -> float:
    """Return the smallest number in the array"""
    return min(array)


def maximum(array: list[float]) -> float:
    """Return the largest number in the array"""
    return max(array)


def sign(x: float) -> int:
    """Return the sign of x (-1, 0, or 1)"""
    return (x > 0) - (x < 0)


def clamp(x: float, min_val: float, max_val: float) -> float:
    """Clamp x to be between min_val and max_val"""
    if min_val > max_val:
        raise ValueError("min_val must be <= max_val")
    return max(min_val, min(x, max_val))


def round_to(x: float, n: int = 0) -> float:
    """Round x to n decimal places (default n is 0)"""
    return round(x, n)


def absolute(x: float) -> float:
    """Return the absolute value of the float x"""
    return stdlib_math.fabs(x)


def sqrt(x: float) -> float:
    """Return the square root of x"""
    return stdlib_math.sqrt(x)


# === Rounding Functions ===


def ceil(x: float) -> int:
    """Return the ceiling of x as an integer. This is the smallest integer >= x"""
    return stdlib_math.ceil(x)


def floor(x: float) -> int:
    """Return the floor of x as an integer. This is the largest integer <= x"""
    return stdlib_math.floor(x)


def trunc(x: float) -> int:
    """Truncate the real x to the nearest integer toward 0"""
    return stdlib_math.trunc(x)


# === Floating Point Functions ===


def copysign(x: float, y: float) -> float:
    """Return a float with the magnitude (absolute value) of x but the sign of y"""
    return stdlib_math.copysign(x, y)


def frexp(x: float) -> tuple[float, int]:
    """Return the mantissa and exponent of x, as pair (m, e). m is a float and e is an int, such that x = m * 2.**e"""
    return stdlib_math.frexp(x)


def ldexp(x: float, i: int) -> float:
    """Return x * (2**i). This is essentially the inverse of frexp()"""
    return stdlib_math.ldexp(x, i)


def modf(x: float) -> tuple[float, float]:
    """Return the fractional and integer parts of x. Both results carry the sign of x and are floats"""
    return stdlib_math.modf(x)
