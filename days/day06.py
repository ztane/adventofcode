from helpers import *

d = get_aoc_data(day=6)


def part1():
    counters = [Counter() for i in range(len('bgpmxqws'))]
    for i in d.lines():
        for j, c in enumerate(i):
            counters[j].update(c)

    message = ''.join([c.most_common(1)[0][0] for c in counters])
    print(message)


def part2():
    counters = [Counter() for i in range(len('bgpmxqws'))]
    for i in d.lines():
        for j, c in enumerate(i):
            counters[j].update(c)

    message = ''.join([c.most_common()[-1][0] for c in counters])
    print(message)

