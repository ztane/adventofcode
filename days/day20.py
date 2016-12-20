from helpers import *

d = get_aoc_data(day=20)


def read_ranges(datalines, max_ip=4294967295):
    input_ranges = []
    for i in datalines:
        start, end = map(int, i.split('-'))
        input_ranges.append((start, end))

    input_ranges.append((max_ip + 1, max_ip + 1))
    return sorted(input_ranges)


def solve_part1(ranges):
    lowest_candidate = 0

    start = None
    for start, end in ranges:
        if start > lowest_candidate:
            return lowest_candidate

        lowest_candidate = max(lowest_candidate, end + 1)

    return None


assert solve_part1(read_ranges(
    '''
    5-8
    0-2
    4-7
    '''.strip().splitlines(), max_ip=9)) == 3


def part1():
    print('answer is', solve_part1(read_ranges(d.lines)))


def solve_part2(ranges):
    lowest_not_covered = 1
    n_addresses_not_covered = 0
    for start, end in ranges:
        if start > lowest_not_covered:
            n_addresses_not_covered += start - lowest_not_covered

        lowest_not_covered = max(lowest_not_covered, end + 1)

    return n_addresses_not_covered


assert solve_part2(read_ranges(
    '''
    5-8
    0-2
    4-7
    '''.strip().splitlines(), max_ip=9)) == 2

def part2():
    print('answer is', solve_part2(read_ranges(d.lines)))

