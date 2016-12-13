from helpers import *
from heapq import *

d = get_aoc_data(day=13)
print(d.data)


@lru_cache(maxsize=None)
def is_free(x, y):
    number = x * x + 3 * x + 2 * x * y + y + y * y + 1352
    binary = format(number, 'b')
    bits = binary.count('1')
    return not (bits & 1)


@total_ordering
class Node:
    def __init__(self, x, y, distance, tgt):
        tx, ty = tgt
        self.min_estimate = abs(x - tx) + abs(y - ty) + distance
        self.data = (x, y, distance)

    def __eq__(self, other):
        return self.min_estimate == other.min_estimate

    def __lt__(self, other):
        return self.min_estimate < other.min_estimate

    def __iter__(self):
        return iter(self.data)


def part1():
    queue = []
    visited =set()
    tgt = 31, 39
    heappush(queue, Node(1, 1, 0, tgt))
    within50 = set()

    while True:
        x, y, dist = heappop(queue)
        if (x, y) == (31, 39):
            print('Answer', dist)
            return

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            newx, newy = x + dx, y + dy
            if newx < 0 or newy < 0 or (newx, newy) in visited:
                continue

            if is_free(newx, newy):
                heappush(queue, Node(newx, newy, dist + 1, tgt))

        visited.add((x, y))
        print(dist)


for i in range(10):
    for j in range(10):
        print('# '[is_free(j, i)], end='')
    print()


def part2():
    queue = []
    visited =set()
    tgt = 1000, 1000
    heappush(queue, Node(1, 1, 0, tgt))
    within50 = set()

    while queue:
        x, y, dist = heappop(queue)
        if (x, y) == (31, 39):
            print('Answer', dist)
            return

        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            newx, newy = x + dx, y + dy
            if newx < 0 or newy < 0 or (newx, newy) in visited:
                continue

            if is_free(newx, newy) and dist < 50:
                heappush(queue, Node(newx, newy, dist + 1, tgt))

        visited.add((x, y))
        if dist <= 50:
            within50.add((x, y))
        print(dist)
    print(len(within50))
