import csv
import customtkinter as ctk
import collections.abc as c

"""
csv형식
key,ko,en,{언어코드},...
"""


class LangManager:
    """언어의 데이터를 관리하는 클래스, 위젯의 언어를 번경시키기 위해 사용됨"""

    _data: dict[str, dict[str, str]] = {}
    _subscribers: list[tuple[str, c.Callable[[str], None]]] = []
    _lang: str | None = None

    @classmethod
    def get_text(cls, key: str) -> str:
        if key not in cls._data:
            return "Key not found"
        elif cls._lang not in cls._data[key]:
            return "Lang not found"
        else:
            return cls._data[key][cls._lang]

    @classmethod
    def init(cls, path: str):
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = row.pop("key")
                cls._data[key] = row

    @classmethod
    def subscribe(
        cls, key: str, callback: ctk.StringVar | c.Callable[[str], None]
    ) -> c.Callable[[], None]:
        if isinstance(callback, ctk.StringVar):
            item = (key, lambda value: callback.set(value))
            cls._subscribers.append(item)
            return lambda: cls._subscribers.remove(item)
        else:
            item = (key, callback)
            cls._subscribers.append(item)
            return lambda: cls._subscribers.remove(item)

    @classmethod
    def set_language(cls, lang: str):
        cls._lang = lang
        for key, subscriber in cls._subscribers:
            if key not in cls._data:
                subscriber("Key not found")
            elif lang not in cls._data[key]:
                subscriber("Lang not found")
            else:
                subscriber(cls._data[key][lang])
