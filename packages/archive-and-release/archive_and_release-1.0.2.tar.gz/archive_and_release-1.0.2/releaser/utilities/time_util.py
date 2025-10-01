import logging
from datetime import datetime, timedelta

_logger:logging.Logger = logging.getLogger(__name__)

def getCurrentDateTimeString(date_format:str = "%d/%m/%Y %H:%M:%S") :
    """
    Returns the current date and time as a formatted string.

    Args:
        date_format (str, optional): The format string to use for formatting the date and time. Defaults to "%d/%m/%Y %H:%M:%S".

    Returns:
        str: A string representing the current date and time formatted according to the specified format.
    """
    return datetime.now().strftime(date_format)


def howOld(timestamp:float) -> timedelta:
    """
    Returns the time delta from the given timestamp to now.

    Args:
        timestamp (float): The timestamp to compare against the current time.

    Returns:
        timedelta: A timedelta object representing the difference between the current time and the given timestamp.
    """
    return datetime.today() - datetime.fromtimestamp(timestamp)


def howOldDays(timestamp:int) -> int:
    """
    Returns the number of days old the given timestamp is.

    Args:
        timestamp (int): The timestamp to compare against the current time.

    Returns:
        int: The number of days old the given timestamp is.
    """
    return howOld(timestamp).days