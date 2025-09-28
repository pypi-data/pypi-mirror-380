__all__ = ["year_progress"]

def year_progress() -> float:
    """
    Calculate the percentage of the current year that has elapsed.

    This function computes how far through the current year we are,
    expressed as a percentage from 0 to 100. It uses the current date and time
    compared against the start and end timestamps of the current year.

    Returns:
        float: The percentage of the current year that has elapsed (0-100).

    Example:
        >>> year_progress()
        45.27  # If called on June 14th, for instance
    """
    dt = __import__("datetime").datetime
    now = dt.now()
    start = dt(now.year, 1, 1, 0, 0, 0, 0).timestamp()
    end = dt(now.year, 12, 31, 23, 59, 59, 999999).timestamp()
    return (now.timestamp() - start) / (end - start) * 100
