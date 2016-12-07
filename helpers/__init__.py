from math import *
from itertools import *
from functools import *
from collections import *
from string import *
import operator as op
import re
from aocd import get_data


class Data:
    def __init__(self, data):
        self.data = data

    def lines(self):
        return list(filter(bool, map(str.rstrip, self.data.splitlines())))

    def split(self, separator=', '):
        return self.data.split(separator)


def get_aoc_data(day):
    return Data(get_data(day=day))


def clamp(value, min_, max_):
    if value < min_:
        return min_
    if value > max_:
        return max_
    return value


def ngrams(n, value):
    """
    Given a *sequence*, return its n-grams
    :param value: the value, can be list, tuple, or str
    :return: *generator* of the ngrams
    """

    for i in range(len(value) - n + 1):
        yield value[i:i + n]


def items(thing, *indexes):
    return op.itemgetter(*indexes)(thing)