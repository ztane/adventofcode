from helpers import get_aoc_data

try:
    from gmpy import popcount
except ImportError:
    def popcount(n):
        return bin(n).count('1')

d = get_aoc_data(day=18)


def solve(data, rows):
    data_len = len(data)

    line = int(data.replace('^', '1').replace('.', '0'), 2)

    # it is easier to count 1's, so we subtract traps from safe tiles
    safe_count = data_len * rows - data.count('^')

    # calculate the bitmask for a row
    mask = (1 << data_len) - 1
    for _ in range(rows - 1):
        # need to mask here, as otherwise we would get more and more bits
        line = ((line << 1) ^ (line >> 1)) & mask
        safe_count -= popcount(line)

    return safe_count


assert solve('.^^.^.^^^^', rows=10) == 38


def part1():
    print('answer', solve(d.data, rows=40))


def part2():
    print('answer', solve(d.data, rows=400000))

