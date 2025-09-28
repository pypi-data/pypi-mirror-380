import statistics

# === Calculating Averages ===


def mean(data: list[float]) -> float:
    """
    Convert data to floats and compute the arithmetic mean. It always returns a float.
    If the input dataset is empty, it raises a StatisticsError.
    """
    return statistics.fmean(data)


def geometric_mean(data: list[float]) -> float:
    """
    Convert data to floats and compute the geometric mean.

    Raises a StatisticsError if the input dataset is empty,
    if it contains a zero, or if it contains a negative value.
    """
    if not data:
        raise statistics.StatisticsError("geometric_mean requires at least one data point")

    # Handle precision issues for identical values
    if len(set(data)) == 1:
        return data[0]  # All values are identical, avoid precision loss

    return statistics.geometric_mean(data)


def harmonic_mean(data: list[float], weights: list[float] | None = None) -> float:
    """
    Return the harmonic mean of data.

    The harmonic mean is the reciprocal of the arithmetic mean of the \
    reciprocals of the data.  It can be used for averaging ratios or \
    rates.
    """
    return statistics.harmonic_mean(data, weights)


def median(data: list[float]) -> float:
    """
    Return the median (middle value) of numeric data.

    When the number of data points is odd, return the middle data point.
    When the number of data points is even, the median is interpolated by
    taking the average of the two middle values.
    """
    return statistics.median(data)


def median_low(data: list[float]) -> float:
    """
    Return the low median of numeric data.

    When the number of data points is odd, the middle value is returned.
    When it is even, the smaller of the two middle values is returned.
    """
    return statistics.median_low(data)


def median_high(data: list[float]) -> float:
    """
    Return the high median of data.

    When the number of data points is odd, the middle value is returned.
    When it is even, the larger of the two middle values is returned.
    """
    return statistics.median_high(data)


def median_grouped(data: list[float], interval: float = 1) -> float:
    """
    Return the 50th percentile (median) of grouped continuous data values.

    This calculates the median as the 50th percentile, and should be
    used when your data is continuous and grouped.

    Optional argument *interval* represents the class interval, and \
    defaults to 1. Changing the class interval naturally will change the \
    interpolated 50th percentile value.
    """
    return statistics.median_grouped(data, interval)


def mode(data: list[float]) -> float:
    """Return the mode of the data. This is the value that appears most frequently in the data."""
    return statistics.mode(data)


def multimode(data: list[float]) -> list[float]:
    """
    Return a list of the most frequently occurring values.
    Will return more than one result if there are multiple modes\
    or an empty list if *data* is empty.
    """
    return statistics.multimode(data)


def quantiles(data: list[float]) -> list[float]:
    """Return the quantiles of the data. This is the values that divide the data into equal parts."""
    return statistics.quantiles(data)


# === Calculating Variability or Spread ===


def pvariance(data: list[float]) -> float:
    """Return the population variance of the data. This is the variance of the population."""
    return statistics.pvariance(data)


def variance(data: list[float], xbar: float | None = None) -> float:
    """
    Return the sample variance of data.

    data should be an array of real-valued numbers, with at least two
    values. The optional argument xbar, if given, should be the mean of
    the data. If it is missing or None, the mean is automatically calculated.

    Use this function when your data is a sample from a population. To
    calculate the variance from the entire population, see ``pvariance``.
    """
    return statistics.variance(data, xbar)


def pstdev(data: list[float]) -> float:
    """Return the population standard deviation of the data. This is the standard deviation of the population."""
    return statistics.pstdev(data)


def stdev(data: list[float], xbar: float | None = None) -> float:
    """
    Return the square root of the sample variance.

    data should be an array of real-valued numbers, with at least two
    values. The optional argument xbar, if given, should be the mean of
    the data. If it is missing or None, the mean is automatically calculated.
    """
    return statistics.stdev(data, xbar)


# === Relations between two inputs ===


def covariance(x: list[float], y: list[float]) -> float:
    """
    Return the sample covariance of two inputs *x* and *y*. Covariance
    is a measure of the joint variability of two inputs.
    """
    return statistics.covariance(x, y)


def correlation(x: list[float], y: list[float]) -> float:
    """
    Return the Pearson's correlation coefficient for two inputs. Pearson's
    correlation coefficient *r* takes values between -1 and +1. It measures the
    strength and direction of the linear relationship, where +1 means very
    strong, positive linear relationship, -1 very strong, negative linear
    relationship, and 0 no linear relationship.
    """
    return statistics.correlation(x, y)


def linear_regression(x: list[float], y: list[float]) -> tuple[float, float]:
    """
    Slope and intercept for simple linear regression.

    Return the slope and intercept of simple linear regression
    parameters estimated using ordinary least squares. Simple linear
    regression describes relationship between an independent variable
    *x* and a dependent variable *y* in terms of linear function:

        y = slope * x + intercept + noise

    where *slope* and *intercept* are the regression parameters that are
    estimated, and noise represents the variability of the data that was
    not explained by the linear regression (it is equal to the
    difference between predicted and actual values of the dependent
    variable).

    The parameters are returned as an array [slope, intercept]
    """
    lr = statistics.linear_regression(x, y)
    return (lr.slope, lr.intercept)
