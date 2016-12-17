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
from heapq import *
import re
import operator as op
from aocd import get_data


class Data:
    def __init__(self, data):
        self.data = data.rstrip('\n\r')

    @property
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


def to_ints(container):
    """
    Return the given items as ints, in the same container type

    :param container: the items
    :return: the items as ints
    """

    t = type(container)
    return t(map(int, container))


def to_floats(container):
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


_parser_conversions = {
    'int': (int, '-?\d+'),
    'str': (str, '.*?'),
}


class Parser:
    """
    A parser class for parsing fields from a single
    formatted input string.
    """
    def __init__(self, fmt, verbatim_ws=False):
        """
        Initialize the parser class, with given format

        :param fmt: the format string
        :param verbatim_ws: if false, spaces are replaced with
            \s+, if true, space characters must match exactly
        """
        regex = ''
        pos = 0

        self.matched = False
        self.items = ()
        self.conversions = []

        while pos < len(fmt):
            c = fmt[pos]
            pos += 1
            if c == '<':
                if fmt[pos] == '<':
                    regex += r'\<'
                    pos += 1
                else:
                    end = fmt.index('>', pos)
                    pattern = fmt[pos:end] or 'str'
                    conversion, _, pattern = pattern.partition(':')
                    convfunc, default_re = _parser_conversions[conversion]
                    if not pattern:
                        pattern = default_re
                    regex += '({})'.format(pattern)
                    self.conversions.append(convfunc)
                    pos = end + 1

            else:
                if c == ' ' and not verbatim_ws:
                    regex += r'\s+'
                else:
                    regex += re.escape(c)

        self.regex = re.compile(regex)

    def __call__(self, string):
        """
        Match the given string agains the pattern, and set results
        :param string: the string
        :return: self for chaining and truth-value checking
        """
        m = self.regex.fullmatch(string)
        self.matched = bool(m)
        if m:
            self.items = tuple(
                self._convert(m, convfunc, group)
                for (group, convfunc) in enumerate(self.conversions, 1))
        else:
            self.items = ()

        return self

    def for_lines(self, lines):
        for line in lines:
            yield tuple(self(line))

    def _convert(self, match, convfunc, group):
        val = match.group(group)
        if val is not None:
            return convfunc(val)
        return None

    def __bool__(self):
        return self.matched

    def __iter__(self):
        if not self.matched:
            raise ValueError('The pattern didn\'t match')

        return iter(self.items)

    def __len__(self):
        if not self.matched:
            raise ValueError('The pattern didn\'t match')

        return len(self.items)

    def __getitem__(self, i):
        if not self.matched:
            raise ValueError('The pattern didn\'t match')

        return self.items[i]




@total_ordering
class Node:
    __slots__ = ('heuristic', 'distance', 'state')

    def __init__(self, heuristic, distance, state):
        self.heuristic = heuristic
        self.distance = distance
        self.state = state

    def __eq__(self, other):
        return ((self.heuristic, self.distance) ==
                (other.heuristic, other.distance))

    def __lt__(self, other):
        return (self.heuristic, self.distance) < (other.heuristic, other.distance)

    def __iter__(self):
        return iter((self.heuristic, self.distance, self.state))


def a_star_solve(origin,
                 *,
                 target=None,
                 max_distance=None,
                 neighbours,
                 heuristic=None,
                 is_target=None,
                 find_all=False):

    if max_distance is None:
        max_distance = 2 ** 32

    if not heuristic:
        heuristic = lambda node, target: 0

    queue = [Node(heuristic(origin, target), 0, origin)]
    visited = {origin}

    if not is_target:
        is_target = lambda n: n == target

    cnt = 0
    all_routes = []
    while queue:
        hx, distance, node = heappop(queue)
        if is_target(node):
            if not find_all:
                return distance, node
            else:
                all_routes.append((distance, node))
                continue

        visited.add(node)
        for d_dist, node in neighbours(node):
            if node in visited:
                continue

            if distance + d_dist <= max_distance:
                heappush(queue, Node(heuristic(node, target),
                                     distance + d_dist, node))
                cnt += 1

    print(cnt, 'iterations')
    if find_all:
        return all_routes
    return len(visited)


chained = chain.from_iterable


def lcm(a, b):
    """
    Returns the least common multiple of the 2 numbers
    :param a: number
    :param b: another
    :return: the lcm
    """
    return (a * b) // gcd(a, b)


def better_translator(table):
    strings = '|'.join(re.escape(i) for i in table.keys())
    pattern = re.compile(strings)

    def replacement(m):
        return table[m.group(0)]

    def translate(s):
        return pattern.sub(replacement, s)

    return translate


def md5digest(s):
    try:
        s = s.encode()
    except AttributeError:
        pass
    return md5(s).hexdigest()
