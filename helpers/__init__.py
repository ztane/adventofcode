from math import *
from itertools import *
from functools import *
from collections import *


def _set_input(filename):
    global _input_filename
    _input_filename = filename

def input_file():
    with open(_input_filename) as f:
        return f.read().strip()

def input_lines():
    return list(filter(bool, map(str.strip, input_file().splitlines())))

def input_split(separator=', '):
    return input_file().split(separator)

def clamp(value, min_, max_):
    if value < min_:
        return min_
    if value > max_:
        return max_
    return value
