from helpers import *
import sys
sys.setrecursionlimit(10000)
d = get_aoc_data(day=11)
print(d.data)

floor_components = (
    (3, 1),
    (0, 2),
    (2, 2),
    (0, 0)
)

#floor_components = (
#    (0, 2),
#    (1, 0),
#    (1, 0),
#    (0, 0)
#)



def fries(comps):
    for g, c in comps:
        if g and g < c:
            return True

    return False


minimums = {
    (((0, 0), (0, 0), (0, 0), (5, 5)), 3): (0, []),
    (((0, 0), (0, 0), (0, 0), (2, 2)), 3): (0, []),
    (((0, 0), (0, 0), (0, 0), (7, 7)), 3): (0, [])
}

currently_visited = set()


def get_min(comps, floor):
    try:
        return minimums[comps, floor]
    except KeyError:
        pass

    if fries(comps):
        return 100000000, []

    minimum = 100000000
    minimum_tail = []
    for move in (1, -1):
        if not (0 <= floor + move <= 3):
            continue

        if move > 0:
            order = ((1, 1), (2, 0), (0, 2), (0, 1), (1, 0))
        else:
            order = ((0, 1), (1, 0), (1, 1), (2, 0), (0, 2))

        for i, (ge, ce) in enumerate(order):
            g, c = comps[floor]
            if g < ge or c < ce:
                continue

            comps_copy = list(comps)
            comps_copy[floor] = g - ge, c - ce
            new_floor = floor + move
            tg, tc = comps_copy[new_floor]
            comps_copy[new_floor] = tg + ge, tc + ce
            floors_t = (tuple(comps_copy), new_floor)

            if floors_t in currently_visited:
                continue

            currently_visited.add(floors_t)
            score, tail = get_min(floors_t[0], new_floor)
            currently_visited.discard(floors_t)

            if score + 1 < minimum:
                minimum = score + 1
                minimum_tail = [(ge, ce, move)] + tail

            # can't do better
            if minimum <= 1:
                minimums[comps, floor] = minimum, minimum_tail
                return minimum, minimum_tail

    minimums[comps, floor] = minimum, minimum_tail
    return minimum, minimum_tail


def solve():
    print(get_min(floor_components, 0))
    print(len(minimums))


def part1():
    solve()


def part2():
    global floor_components
    floor_components = (
        (5, 3),
        (0, 2),
        (2, 2),
        (0, 0)
    )
    solve()
