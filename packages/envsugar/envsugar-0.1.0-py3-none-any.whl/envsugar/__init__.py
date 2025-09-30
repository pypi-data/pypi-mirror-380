import os

def __getattr__(name):
    return os.environ.get(name)

def __dir__():
    return os.environ.keys()