from helpers import get_aoc_data, md5digest, a_star_solve

d = get_aoc_data(day=17)

directions = list(enumerate((('U', 0, -1),
                             ('D', 0, 1),
                             ('L', -1, 0),
                             ('R', 1, 0))))


def solve(data, find_max_length=False):
    def neighbours(state):
        route, x, y = state
        route_hash = md5digest(data + route)
        for i, (direction, dx, dy) in directions:
            if route_hash[i] >= 'b':
                nx = x + dx
                ny = y + dy
                if 0 <= nx <= 3 and 0 <= ny <= 3:
                    nr = route + direction
                    yield (1, (nr, nx, ny))

    rv = a_star_solve(
        origin=('', 0, 0),
        is_target=lambda node: node[1] == 3 and node[2] == 3,
        neighbours=neighbours,
        # simple manhattan distance
        heuristic=lambda node, *dummy: abs(node[1] - 3) + abs(node[2] - 3),
        find_all=find_max_length)

    if not find_max_length:
        return rv[1][0]
    else:
        return max(rv)[0]


def part1():
    print('answer', solve(d.data))


def part2():
    print('answer', solve(d.data, find_max_length=True))

