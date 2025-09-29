from .typing import *
from .external import *


__all__ = [
    "Time",
    "get_current_time",
]


@dataclass
class Time:
    year: int
    month: int
    day: int
    hour: int
    minute: int
    second: int


def get_current_time(
)-> Time:
    
    current_datetime = datetime.now()
    
    return Time(
        year = current_datetime.year,
        month = current_datetime.month,
        day = current_datetime.day,
        hour = current_datetime.hour,
        minute = current_datetime.minute,
        second = current_datetime.second,
    )