from helpers import *
from heapq import *

d = get_aoc_data(day=13)


@lru_cache(maxsize=None)
def is_free(x, y, *, own_number=int(d.data)):
    if x < 0 or y < 0:
        return False

    number = x * x + 3 * x + 2 * x * y + y + y * y + own_number
    one_bits = format(number, 'b').count('1')
    return not (one_bits & 1)


def neighbours(x_y):
    x, y = x_y
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if nx >= 0 and ny >= 0 and is_free(nx, ny):
            yield (1, (nx, ny))


def part1():
    print('solution to part 1 is',
          a_star_solve(
              (1, 1),
              target=(31, 39),
              neighbours=neighbours,
              heuristic=lambda node, target:
                  abs(node[0] - target[0]) + abs(node[1] - target[1])))


def part2():
    print('solution to part 2 is',
          a_star_solve((1, 1), max_distance=50, neighbours=neighbours))
