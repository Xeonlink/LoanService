import os


def swapkv(d: dict):
    return {v: k for k, v in d.items()}


def readlines(*path):
    with open(os.path.join(*path), "r") as f:
        return "".join(f.readlines())
