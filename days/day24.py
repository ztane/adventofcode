from helpers import *
import sys


the_map = get_aoc_data(day=24).lines

locations = {}

height = len(the_map)
width = len(the_map[0])

for y in range(len(the_map)):
    for x in range(len(the_map[y])):
        if the_map[y][x].isdigit():
            locations[the_map[y][x]] = (x, y)


all_markers = [str(i) for i in range(0, len(locations))]


def find_distance(start_marker, end_marker):
    origin = locations[start_marker]
    destination = locations[end_marker]

    def neighboring_nodes(node):
        x, y = node
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < width and 0 <= ny < height and the_map[ny][nx] != '#':
                yield 1, (nx, ny)

    return a_star_solve(
        origin,
        target=destination,
        heuristic=lambda o, t: abs(t[0] - o[0]) + abs(t[1] - o[1]),
        neighbours=neighboring_nodes)


print('precalculating shortest paths')
distance = {}
for start, goal in combinations(all_markers, 2):
    shortest = find_distance(start, goal)[0]
    distance[start, goal] = distance[goal, start] = shortest


def solve(to_origin=False):
    min_len = sys.maxsize
    for visit_order in permutations(all_markers[1:]):
        if to_origin:
            path = ('0', *visit_order, '0')
        else:
            path = ('0', *visit_order)

        length = sum(distance[start, goal] for start, goal in ngrams(2, path))
        min_len = min(min_len, length)

    return min_len


def part1():
    print('answer is', solve())


def part2():
    print('answer is', solve(to_origin=True))
