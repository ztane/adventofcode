import re

from collections import deque
from helpers import get_aoc_data, Parser

d = get_aoc_data(day=11)
lineparser = Parser('The <> floor contains <>.')

states = []
for i in d.lines:
    _, items = lineparser(i)
    items_split = re.split(', | and ', items)
    generators, microchips = 0, 0

    for j in items_split:
        if j != 'nothing relevant':
            if 'generator' in j:
                generators += 1
            else:
                microchips += 1

    states.append((generators, microchips))


def fries(comps):
    """
    Returns true if something will be fried in the state
    """
    for g, c in comps:
        if g and g < c:
            return True

    return False


def solve(components):
    open_nodes = deque()
    open_nodes.append((components, 0, 0))

    visited = set()

    while True:
        comps, floor, distance = open_nodes.popleft()
        for move in (1, -1):
            new_floor = floor + move
            if not (0 <= new_floor <= 3):
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
                tg, tc = comps_copy[new_floor]
                comps_copy[new_floor] = tg + ge, tc + ce
                floors_t = (tuple(comps_copy), new_floor)

                if floors_t not in visited and not fries(comps_copy):
                    visited.add(floors_t)
                    open_nodes.append(floors_t + (distance + 1,))
                    if comps[0:3] == ((0, 0), (0, 0), (0, 0)):
                        print(distance)
                        return

def part1():
    solve(tuple(states))

def part2():
    """
    Add 2 generators, chips
    """

    states[0] = states[0][0] + 2, states[0][1] + 2
    solve(tuple(states))
