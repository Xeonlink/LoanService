import csv
import customtkinter as ctk
from collections.abc import Callable

"""
csv형식
key,ko,en,{언어코드},...
"""


class I18n:
    """언어의 데이터를 관리하는 클래스, 위젯의 언어를 번경시키기 위해 사용됨"""

    _language_file_path: str | None = None
    _data: dict[str, dict[str, str]] = {}
    _subscribers: list[tuple[str, Callable[[str], None]]] = []
    lang: str | None = None

    @classmethod
    def get_text(cls, key: str) -> str:
        if key not in cls._data:
            return "Key not found"
        elif cls.lang not in cls._data[key]:
            return "Lang not found"
        else:
            text = cls._data[key][cls.lang]
            return "\n".join(text.split("\\n"))

    @classmethod
    def init(cls, path: str | None = None) -> tuple[bool, str | None]:
        """
        언어 데이터를 초기화한다.

        :param path: 언어 데이터가 저장된 csv파일의 경로
        :return: 성공시 (True, None), 실패시 (False, 에러메시지)
        """
        if path is None:
            path = cls._language_file_path

        if path is None:
            return (False, "Path is not set")

        try:
            with open(path, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    key = row.pop("key")
                    cls._data[key] = row
            cls._language_file_path = path
            return (True, None)
        except Exception as e:
            print(e)
            return (False, str(e))

    @classmethod
    def subscribe(
        cls, key: str, callback: ctk.StringVar | Callable[[str], None]
    ) -> Callable[[], None]:
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
        cls.lang = lang
        for key, subscriber in cls._subscribers:
            if key not in cls._data:
                subscriber("Key not found")
            elif lang not in cls._data[key]:
                subscriber("Lang not found")
            else:
                subscriber(cls._data[key][lang])
