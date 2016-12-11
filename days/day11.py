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
        item_states, elevator_door, distance = open_nodes.popleft()
        for move in (1, -1):
            new_floor = elevator_door + move
            if not (0 <= new_floor <= 3):
                continue

            if move > 0:
                order = ((1, 1), (2, 0), (0, 2), (0, 1), (1, 0))
            else:
                order = ((0, 1), (1, 0), (1, 1), (2, 0), (0, 2))

            for i, (ge, ce) in enumerate(order):
                g, c = item_states[elevator_door]
                if g < ge or c < ce:
                    continue

                new_item_state = list(item_states)
                new_item_state[elevator_door] = g - ge, c - ce
                tg, tc = new_item_state[new_floor]
                new_item_state[new_floor] = tg + ge, tc + ce
                new_item_state = tuple(new_item_state)

                if ((new_item_state, new_floor) not in visited
                    and not fries(new_item_state)):

                    visited.add((new_item_state, new_floor))
                    open_nodes.append(
                        (new_item_state, new_floor, distance + 1,))
                    if new_item_state[0:3] == ((0, 0), (0, 0), (0, 0)):
                        print(distance + 1)
                        return


def part1():
    solve(tuple(states))


def part2():
    """
    Add 2 generators, chips
    """

    states[0] = states[0][0] + 2, states[0][1] + 2
    solve(tuple(states))
