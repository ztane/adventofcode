import re
from itertools import count
from collections import deque
from helpers import get_aoc_data, Parser
from functools import lru_cache
import itertools

d = get_aoc_data(day=11)

lineparser = Parser('The <> floor contains <>.')

next_element_bit = count()
element_numbers = {}
def get_element_number(element):
    if element not in element_numbers:
        element_numbers[element] = 1 << next(next_element_bit)
    return element_numbers[element]


max_bit = 16

def parse_state(state):
    states = []
    for i in state.splitlines():
        _, items = lineparser(i)
        items_split = re.split(',? and |, ', items)
        generators, microchips = 0, 0

        for j in items_split:
            if j != 'nothing relevant':
                if 'generator' in j:
                    el = j.split(' ')[1]
                    generators |= get_element_number(el)
                else:
                    el = j.split(' ')[1].partition('-')[0]
                    microchips |= get_element_number(el)

        states.append((generators << 8) +  microchips)

    return states


def fries(state):
    """
    Returns true if something will be fried in the state
    """
    for items in state:
        gens = items >> 8
        chips = items & 0xFF

        if gens and (gens | chips) != gens:
            return True

    return False


@lru_cache(maxsize=None)
def get_combinations(floor_state, up):
    bits_set = []
    for bit in range(max_bit):
        if floor_state & (1 << bit):
            bits_set.append(1 << bit)

    two_items = list(sum(i) for i in itertools.combinations(bits_set, 2))
    one_item = bits_set
    if up:
        return two_items + one_item

    return one_item + two_items


def solve(components):
    open_nodes = deque()
    open_nodes.append((components, 0, 0))
    visited = set()

    while True:
        try:
            item_states, elevator_door, distance = open_nodes.popleft()
        except:
            raise

        for move in (1, -1):
            new_floor = elevator_door + move
            if not (0 <= new_floor <= 3):
                continue

            floor_state = item_states[elevator_door]
            for item_bits in get_combinations(floor_state, up=move==1):
                new_item_state = list(item_states)
                new_item_state[elevator_door] = floor_state & ~item_bits
                new_item_state[new_floor] = new_item_state[new_floor] | item_bits
                new_item_state = tuple(new_item_state)
                if ((new_item_state, new_floor) not in visited and not fries(new_item_state)):
                    visited.add((new_item_state, new_floor))
                    open_nodes.append(
                        (new_item_state, new_floor, distance + 1,))
                    if new_item_state[0:3] == (0, 0, 0):
                        print(distance + 1)
                        return


def part1():
    data = tuple(parse_state(d.data))
    solve(data)

def part2():
    data = parse_state(d.data)
    extras = get_element_number('elerium') | get_element_number('dilithium')
    data[0] |= extras | (extras << 8)
    solve(tuple(data))
