from collections import Counter

from helpers import get_aoc_data

d = get_aoc_data(day=6)


def part1():
    counters = [Counter() for _ in range(len('bgpmxqws'))]
    for line in d.lines():
        for ctr, char in zip(counters, line):
            ctr.update(char)

    message = ''.join([c.most_common(1)[0][0] for c in counters])
    print(message)


def part2():
    counters = [Counter() for _ in range(len('bgpmxqws'))]
    for line in d.lines():
        for ctr, char in zip(counters, line):
            ctr.update(char)

    message = ''.join([c.most_common()[-1][0] for c in counters])
    print(message)

