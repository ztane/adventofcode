from helpers import *
# import numpy as np

d = get_aoc_data(day=7)


def has_abba(net):
    """
    Return true if given net has ABBA
    :param net: the super/hypernet
    :return: True if it has ABBA
    """

    for p in ngrams(4, net):
        if items(p, 0, 1) == items(p, 3, 2) and p[0] != p[1]:
            return True


def netsplit(s):
    """
    Return supers, hypers
    :param s: the string
    :return: sequence of (supers, hypers)
    """
    nets = re.split('\\[(.*?)]', s)
    rv = [[], []]
    for i, net in enumerate(nets):
        rv[i % 2].append(net)

    return rv


def part1():
    cnt = 0
    for i in d.lines():
        supers, hypers = netsplit(i)

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
    for p in ngrams(3, net):
        if p[0] == p[2] and p[0] != p[1]:
            yield p[1] + p[0] + p[1]


def part2():
    cnt = 0
    for i in d.lines():
        supers, hypers = netsplit(i)

        for sn in supers:
            for bab in get_babs(sn):
                if any(bab in hyper for hyper in hypers):
                    cnt += 1
                    break

    print(cnt)

