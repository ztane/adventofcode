from helpers import get_aoc_data, get_ints, lcm, Parser

d = get_aoc_data(day=15)


def parse_starting_state(data):
    disc_parser = Parser('Disc #<int> has <int> positions; '
                         'at time=<int>, it is at position <int>.')
    discs = []
    for j, i in enumerate(data.strip().splitlines(), 1):
        _, positions, t, start = disc_parser(i)
        discs.append((positions, (start + j - t) % positions))

    return discs


def solve(state):
    t = 0
    min_step = 1
    disc_set = set(parse_starting_state(state))
    while disc_set:
        for d, p in list(disc_set):
            if not (p + t) % d:
                # though not strictly needed with my input as mine are
                # prime numbers, we should use lcm here in case they're not
                min_step = lcm(min_step, d)
                disc_set.discard((d, p))
                print('synced disc at', t, '- min step', min_step)
                continue

        if disc_set:
            t += min_step

    return t


assert solve("""
Disc #1 has 5 positions; at time=0, it is at position 4.
Disc #2 has 2 positions; at time=0, it is at position 1.
""") == 5


def part1():
    print('solution', solve(d.data))


part2_extra = """
Disc #7 has 8191 positions; at time=0, it is at position 427.
"""

def part2():
    print('solution', solve(d.data + part2_extra))
