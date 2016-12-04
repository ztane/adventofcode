from helpers import *

d = get_aoc_data(day=3)

def is_triangle(numbers):
    for j in range(3):
        l = list(numbers)
        this = l.pop(j)
        if this >= sum(l):
            return False
    return True


def part1():
    count = 0

    for i in d.lines():
        numbers = list(map(int, i.split()))
        count += is_triangle(numbers)

    print(count)


def part2():
    count = 0

    def gen():
        for i in d.lines():
            yield list(map(int, i.split()))

    horizontal = zip(*gen())
    chained = list(chain.from_iterable(horizontal))
    for i in range(0, len(chained), 3):
        numbers = chained[i:i + 3]
        count += is_triangle(numbers)

    print(count)

