import math as stdlib_math

# === Square Root ===


def isqrt(x: int) -> int:
    """Return the integer part of the square root of the input"""
    return stdlib_math.isqrt(x)


def factorial(x: int) -> int:
    """Find x!. Raise a ValueError if x is negative or non-integral"""
    return stdlib_math.factorial(x)


# === Number Theory Functions ===


def gcd(a: int, b: int) -> int:
    """Greatest Common Divisor of a and b"""
    return stdlib_math.gcd(a, b)


def lcm(a: int, b: int) -> int:
    """Least Common Multiple of a and b"""
    return stdlib_math.lcm(a, b)


def combination(n: int, k: int) -> int:
    """
    Number of ways to choose k items from n items without repetition and without order (binomial coefficient)
    """
    return stdlib_math.comb(n, k)


def permutation(n: int, k: int | None = None) -> int:
    """
    Number of ways to choose k items from n items without repetition and with order. If k is None, defaults to n.
    """
    return stdlib_math.perm(n, k)
