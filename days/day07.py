from helpers import *
# import numpy as np

d = get_aoc_data(day=7)


def has_abba(s):
    for i in range(len(s) - 3):
        part = s[i:i+4]
        if part[0] == part[3] and part[1] == part[2] and part[0] != part[1]:
            return True


def part1():
    cnt = 0
    for i in d.lines():
        seqs = re.split('\\[(.*?)]', i)
        has_abba_in_supernet = False

        for j, item in enumerate(seqs):
            # hypernet/supernet
            if j % 2 and has_abba(item):
                # has *an* ABBA in hypernet
                break

            else:
                # or the value for supernets
                has_abba_in_supernet |= bool(has_abba(item))

        else:
            cnt += has_abba_in_supernet

    print(cnt)


def get_babs(s):
    """
    For each ABA, yield the corresponding BAB
    :param s: the string where to find ABAs
    :return: generator of BABs
    """
    for i in range(len(s) - 2):
        part = s[i:i+3]
        if part[0] == part[2] and part[0] != part[1]:
            yield part[1] + part[0] + part[1]


def part2():
    cnt = 0
    for i in d.lines():
        seqs = re.split('\\[(.*?)]', i)
        babs = []
        hypernets = []

        for j, item in enumerate(seqs):
            # supernet/hypernet?
            if j % 2:
                # supernet
                babs.extend(get_babs(item))
            else:
                # hypernet
                hypernets.append(item)

        for hypernet in hypernets:
            for bab in babs:
                if bab in hypernet:
                    cnt += 1
                    break

    print(cnt)

