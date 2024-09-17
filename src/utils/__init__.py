import os
from .LangManager import LangManager


class Utils:
    @classmethod
    def readlines(cls, *path):
        with open(os.path.join(*path), "r") as f:
            return "".join(f.readlines())
