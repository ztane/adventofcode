import re

from helpers import get_aoc_data, get_ints

d = get_aoc_data(day=9)

d.data = '(6x2)A(1x2)B'
repetition_marker = re.compile(r'\(\d+x\d+\)')


def get_length(s, recursive=False):
    total = 0
    pos = 0
    while pos < len(s):
        m = repetition_marker.match(s, pos)
        if m:
            length, repeats = get_ints(m.group(0))
            pos += len(m.group(0))

            if recursive:
                total += repeats * get_length(s[pos:pos+length], True)
            else:
                total += repeats * length

            pos += length

        else:
            total += 1
            pos += 1

    return total


def part1():
    print('uncompressed length is', get_length(d.data))


def part2():
    print('recursively uncompressed length is', get_length(d.data, True))
