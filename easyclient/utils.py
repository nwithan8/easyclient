from datetime import datetime, timedelta
from typing import Union, List, Iterable

from pytz import timezone


def make_plural(word, count: int, suffix_override: str = 's') -> str:
    if count > 1:
        return f"{word}{suffix_override}"
    return word


def datetime_to_string(datetime_object: datetime, string_format: str = "%Y-%m-%d") -> Union[str, None]:
    """
    Convert a datetime.datetime object to a string

    :param datetime_object: Datetime.datetime object to convert
    :type datetime_object: datetime
    :param string_format: Date format to use
    :type string_format: str
    :return: Date in string format
    :rtype: str
    """
    if not datetime_object:
        return None
    return datetime_object.strftime(__format=string_format)


def milliseconds_to_minutes_seconds(milliseconds: int) -> str:
    seconds = int(milliseconds / 1000)
    minutes = int(seconds / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = int(seconds % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    return f"{minutes}:{seconds}"


def now_plus_milliseconds(milliseconds: int, timezone_code: str = None) -> datetime:
    if timezone_code:
        now = datetime.now(timezone(timezone_code))  # will raise exception if invalid timezone_code
    else:
        now = datetime.now()
    return now + timedelta(milliseconds=milliseconds)
