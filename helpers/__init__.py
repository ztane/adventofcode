# noinspection PyUnresolvedReferences
from math import *
# noinspection PyUnresolvedReferences
from itertools import *
# noinspection PyUnresolvedReferences
from functools import *
# noinspection PyUnresolvedReferences
from collections import *
# noinspection PyUnresolvedReferences
from string import *
# noinspection PyUnresolvedReferences
from hashlib import md5
# noinspection PyUnresolvedReferences
import re
import operator as op
from aocd import get_data


class Data:
    def __init__(self, data):
        self.data = data

    def lines(self):
        return list(filter(bool, map(str.rstrip, self.data.splitlines())))

    def split(self, separator=', '):
        return self.data.split(separator)


def get_aoc_data(day):
    """
    Get the wrapped AOC data for a given day

    :param day: the day
    :return: the data
    """
    return Data(get_data(day=day))


def clamp(value, min_, max_):
    """
    Clamp the value so that it is at least min_ and at most max_

    :param value: the value
    :param min_: the minimum
    :param max_: the maximum
    :return: min_, max_, or value, iff min_ <= value <= max_
    """

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
    """
    Return the given indexes of the item as a tuple

    :param thing: the thing to index
    :param indexes: indexes
    :return: tuple of the items
    """
    return op.itemgetter(*indexes)(thing)


def ints(container):
    """
    Return the given items as ints, in the same container type

    :param container: the items
    :return: the items as ints
    """

    t = type(container)
    return t(map(int, container))


def floats(container):
    """
    Return the given items as floats, in the same container type

    :param container: the items
    :return: the items as ints
    """

    t = type(container)
    return t(map(float, container))


def every_nths(iterable, n=2):
    """
    return n lists of every nth elements; first list contains item
    0, second list item 1 and so forth

    :param iterable: the iterable to iterate over. Will be converted
        to a list internally
    :return: list of lists
    """

    as_list = list(iterable)
    return [as_list[i::n] for i in range(n)]


def get_ints(s):
    """
    Return all decimal integers in the given string
    as a sequence

    :param s: a string
    :return: sequence of integers
    """
    return list(map(int, re.findall('\d+', s)))


def draw_display(display_data):
    """
    Draw pixel display (row, column matrix)

    :param display_data: the display data
    :return: None
    """
    row_length = len(display_data[0])
    print('-' * row_length)
    for row in display_data:
        for column in row:
            print([' ', '\033[42m \033[0m'][bool(column)], end='')
        print()
    print('-' * row_length)


