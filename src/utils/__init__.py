from datetime import datetime
import os
import sys


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


def resource_path(relative_path: str) -> str:
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS  # type: ignore
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def _(_):
    """리턴값을 전달하지 않는 함수, lambda에서 return을 생략하기 위해 사용됨"""
    return
