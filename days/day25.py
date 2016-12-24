from typing import List

from helpers import *

d = get_aoc_data(day=22)

lineparser = Parser('/dev/grid/node-x<int>-y<int> <int>T <int>T <int>T <int>%')
disktuple = namedtuple('x y size used avail percent')


def read_input(data) -> List[disktuple]:
    return [disktuple(lineparser(i)) for i in data]


def solve(data):
    d = read_input(data)
    avail = sorted(d, key=lambda d: d.avail)
    used = sorted(d, key=lambda d: d.used)
    cnt = 0
    for i in used:
        for j in avail:
            if j.avail >= i.used:
                cnt += 1

    return cnt

assert solve(21) == 42


def part1():
    print('answer is', solve(d.data[1:]))


def part2():
    0 and print('answer is', solve(d.data))
