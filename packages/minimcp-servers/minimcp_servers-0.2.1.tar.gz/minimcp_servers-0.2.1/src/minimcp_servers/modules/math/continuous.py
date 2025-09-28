import math as stdlib_math

# === Trigonometric Functions ===


def sin(x: float) -> float:
    """Return the sine of x (measured in radians)"""
    return stdlib_math.sin(x)


def cos(x: float) -> float:
    """Return the cosine of x (measured in radians)"""
    return stdlib_math.cos(x)


def tan(x: float) -> float:
    """Return the tangent of x (measured in radians)"""
    return stdlib_math.tan(x)


def asin(x: float) -> float:
    """Return the arc sine (measured in radians) of x. Result is between -pi/2 and pi/2"""
    return stdlib_math.asin(x)


def acos(x: float) -> float:
    """Return the arc cosine (measured in radians) of x. Result is between 0 and pi"""
    return stdlib_math.acos(x)


def atan(x: float) -> float:
    """Return the arc tangent (measured in radians) of x. Result is between -pi/2 and pi/2"""
    return stdlib_math.atan(x)


def atan2(y: float, x: float) -> float:
    """
    Return the arc tangent (measured in radians) of y/x. Unlike atan(y/x), the signs of both x and y are considered
    """
    return stdlib_math.atan2(y, x)


# === Hyperbolic Functions ===


def sinh(x: float) -> float:
    """Return the hyperbolic sine of x"""
    return stdlib_math.sinh(x)


def cosh(x: float) -> float:
    """Return the hyperbolic cosine of x"""
    return stdlib_math.cosh(x)


def tanh(x: float) -> float:
    """Return the hyperbolic tangent of x"""
    return stdlib_math.tanh(x)


def asinh(x: float) -> float:
    """Return the inverse hyperbolic sine of x"""
    return stdlib_math.asinh(x)


def acosh(x: float) -> float:
    """Return the inverse hyperbolic cosine of x"""
    return stdlib_math.acosh(x)


def atanh(x: float) -> float:
    """Return the inverse hyperbolic tangent of x"""
    return stdlib_math.atanh(x)


# === Exponential Functions ===


def exp(x: float) -> float:
    """Return e raised to the power of x"""
    return stdlib_math.exp(x)


def expm1(x: float) -> float:
    """
    Return exp(x)-1. This function avoids the loss of precision involved in the
    direct evaluation of exp(x)-1 for small x
    """
    return stdlib_math.expm1(x)


# === Logarithmic Functions ===


def log(x: float, base: float = stdlib_math.e) -> float:
    """
    Return the logarithm of x to the given base. If the base is not specified,
    returns the natural logarithm (base e) of x
    """
    return stdlib_math.log(x, base)


def log10(x: float) -> float:
    """Return the base 10 logarithm of x"""
    return stdlib_math.log10(x)


def log2(x: float) -> float:
    """Return the base 2 logarithm of x"""
    return stdlib_math.log2(x)


def log1p(x: float) -> float:
    """
    Return the natural logarithm of 1+x (base e). The result is computed in a way
    which is accurate for x near zero
    """
    return stdlib_math.log1p(x)


# === Angular Conversion Functions ===


def degrees(x: float) -> float:
    """Convert angle x from radians to degrees"""
    return stdlib_math.degrees(x)


def radians(x: float) -> float:
    """Convert angle x from degrees to radians"""
    return stdlib_math.radians(x)


# === Distance and Geometric Functions ===


def hypot(x: float, y: float) -> float:
    """
    Return the 2-dimensional euclidean distance, sqrt(x*x + y*y). This is the length of
    the vector from the origin to point (x, y)
    """
    return stdlib_math.hypot(x, y)


def multidimensional_hypot(coordinates: list[float]) -> float:
    """
    Return the multidimensional euclidean distance. This is the length of
    the vector from the origin to point (x, y, z, ...)
    """
    return stdlib_math.hypot(*coordinates)


def dist(p: list[float], q: list[float]) -> float:
    """
    Return the Euclidean distance between two points p and q.

    The points should be specified as sequences (or iterables) of
    coordinates.  Both inputs must have the same dimension.
    """
    return stdlib_math.dist(p, q)


# === Special Functions ===


def gamma(x: float) -> float:
    """Gamma function at x"""
    return stdlib_math.gamma(x)


def lgamma(x: float) -> float:
    """Natural logarithm of absolute value of Gamma function at x"""
    return stdlib_math.lgamma(x)


def erf(x: float) -> float:
    """Error function at x"""
    return stdlib_math.erf(x)


def erfc(x: float) -> float:
    """Complementary error function at x"""
    return stdlib_math.erfc(x)
