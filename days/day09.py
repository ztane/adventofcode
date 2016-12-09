from helpers import *

d = get_aoc_data(day=9)

marker_re = re.compile(r'\((\d+)x(\d+)\)')


def get_length(s, recursive=False):
    total = 0
    pos = 0
    while pos < len(s):
        m = marker_re.match(s, pos)
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

