from typing import List

from helpers import *

d = get_aoc_data(day=22)

lineparser = Parser('/dev/grid/node-x<int>-y<int> <int>T <int>T <int>T <int>%')
disktuple = namedtuple('disktuple', 'x y size used avail percent')


def read_input(data) -> List[disktuple]:
    return [disktuple(*lineparser(i)) for i in data]


def solve(data, part2=False):
    d = read_input(data)
    avail = sorted(d, key=lambda d: d.avail)
    used = sorted(d, key=lambda d: d.used)
    cnt = 0
    for i in used:
        for j in avail:
            if i is not j and j.avail >= i.used and i.used:
                cnt += 1

    if not part2:
        return cnt

    width = max(disk.x for disk in d) + 1
    height = max(disk.y for disk in d) + 1
    min_size = min(disk.size for disk in d)

    wall_map = [[False] * width for _ in range(height)]
    hole = None

    for disk in d:
        wall_map[disk.y][disk.x] = disk.used > min_size
        if disk.used == 0:
            if not hole:
                print('Found hole at {}, {}'.format(disk.x, disk.y))
                hole = disk.x, disk.y
            else:
                print('Error, 2 holes!')
                exit(1)

    def neighboring_nodes(x, y):
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < width and 0 <= ny < height and not wall_map[ny][nx]:
                yield nx, ny

    def neighbours(node):
        gx, gy, hx, hy = node

        for nx, ny in neighboring_nodes(hx, hy):
            if (nx, ny) == (gx, gy):
                # swap hole and goal!
                yield 1, (hx, hy, nx, ny)
            else:
                # just move the hole
                yield 1, (gx, gy, nx, ny)

    return a_star_solve(origin=(width - 1, 0, hole[0], hole[1]),
                        target=(0, 0),
                        heuristic=lambda n, t: (
                            n[0] + n[1]
                            + abs(n[2] - n[0]) + abs(n[3] - n[1])
                            + 0.1 * (n[2] + n[3])
                        ),
                        neighbours=neighbours,
                        is_target=lambda t: t[0] == 0 and t[1] == 0)[0]


def part1():
    print('answer is', solve(d.lines[2:]))


def part2():
    print('answer is', solve(d.lines[2:], part2=True))
