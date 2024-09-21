from datetime import datetime
from collections.abc import Callable
from typing import Any
import os


def swapkv(d: dict):
    return {v: k for k, v in d.items()}


def readlines(*path):
    with open(os.path.join(*path), "r") as f:
        return "".join(f.readlines())


def format_loan_duration(start: datetime, end: datetime):
    if start.year == end.year:
        if start.month == end.month:
            if start.day == end.day:
                return start.strftime("%Y.%m.%d")
            else:
                return f"{start.strftime('%Y.%m.%d')} ~ {end.strftime('%m.%d')}"
        else:
            return f"{start.strftime('%Y.%m.%d')} ~ {end.strftime('%m.%d')}"
    else:
        return f"{start.strftime('%Y.%m.%d')} ~ {end.strftime('%Y.%m.%d')}"


def find[T](getter: Callable[[T], Any], list: list[T]):
    for item in list:
        if getter(item):
            return item
    return None
