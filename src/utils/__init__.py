import os
from .I18n import I18n


class Utils:
    @classmethod
    def readlines(cls, *path):
        with open(os.path.join(*path), "r") as f:
            return "".join(f.readlines())
