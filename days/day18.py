from helpers import get_aoc_data

d = get_aoc_data(day=18)


def solve(data, rows):
    data_len = len(data)

    line = int(data.replace('^', '1').replace('.', '0'), 2)
    safe_count = data.count('.')

    mask = (1 << data_len) - 1
    fmt = '0{}b'.format(data_len)

    for _ in range(rows - 1):
        # need to mask here, as otherwise we would get more and more bits
        line = ((line << 1) ^ (line >> 1)) & mask
        safe_count += format(line, fmt).count('0')

    return safe_count


assert solve('.^^.^.^^^^', rows=10) == 38


def part1():
    print('answer', solve(d.data, rows=40))


def part2():
    print('answer', solve(d.data, rows=400000))

