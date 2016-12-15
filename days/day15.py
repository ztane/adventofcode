from helpers import *

d = get_aoc_data(day=15)


def parse_starting_state(data):
    discs = []
    for j, i in enumerate(data.strip().splitlines(), 1):
        _, positions, _, start = get_ints(i)
        discs.append((positions, (start + j) % positions))

    return discs

def solve(state):
    t = 0
    product = 1
    disc_set = set(parse_starting_state(state))
    while disc_set:
        for d, p in list(disc_set):
            if not (p + t) % d:
                product *= d
                disc_set.discard((d, p))
                print('synced disc at', t, 'product', product)
                continue

        if disc_set:
            t += product

    return t


assert solve("""
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
""") == 5


def part1():
    print('solution', solve(d.data))


part2_extra = """
Disc #6 has 11 positions; at time=0, it is at position 0.
"""


def part2():
    print('solution', solve(d.data + part2_extra))

