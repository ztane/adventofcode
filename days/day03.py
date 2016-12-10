from helpers import get_aoc_data, chained

d = get_aoc_data(day=3)


def is_triangle(numbers):
    a, b, c = sorted(numbers)
    return not c >= a + b


def part1():
    count = 0

    for i in d.lines:
        count += is_triangle(map(int, i.split()))

    print(count)


def part2():
    count = 0

    def gen():
        for i in d.lines:
            yield list(map(int, i.split()))

    horizontal = zip(*gen())
    all_ = list(chained(horizontal))
    for i in range(0, len(all_), 3):
        numbers = all_[i:i + 3]
        count += is_triangle(numbers)

    print(count)

