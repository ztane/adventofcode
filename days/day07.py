import re

from helpers import get_aoc_data, ngrams, every_nths

d = get_aoc_data(day=7)


def has_abba(net):
    """
    Return true if given net has ABBA
    :param net: the super/hypernet
    :return: True if it has ABBA
    """

    for a, b, b2, a2 in ngrams(4, net):
        if (a, b) == (a2, b2) and a != b:
            return True


def netsplit(s):
    """
    Return supers, hypers
    :param s: the string
    :return: sequence of (supers, hypers)
    """
    nets = re.split('\\[(.*?)]', s)
    return every_nths(nets)


def part1():
    cnt = 0
    for i in d.lines:
        supers, hypers = netsplit(i.strip())

        if not any(map(has_abba, supers)):
            continue

        if not any(map(has_abba, hypers)):
            cnt += 1

    print(cnt)


def get_babs(net):
    """
    For each ABA, yield the corresponding BAB
    :param net: the string where to find ABAs
    :return: generator of BABs
    """
    for a, b, a2 in ngrams(3, net):
        if a == a2 and a != b:
            yield b + a + b


def part2():
    cnt = 0
    for i in d.lines:
        supers, hypers = netsplit(i)

        for sn in supers:
            for bab in get_babs(sn):
                if any(bab in hyper for hyper in hypers):
                    cnt += 1
                    break

    print(cnt)

