from helpers import get_aoc_data, md5digest, a_star_solve

d = get_aoc_data(day=17)


def solve(data, find_max_length=False):
    def neighbours(state):
        route, rhash, x, y = state
        for i, (direction, dx, dy) in enumerate(
                [('U', 0, -1), ('D', 0, 1), ('L', -1, 0), ('R', 1, 0)]):
            if rhash[i] >= 'b':
                nx = x + dx
                ny = y + dy
                if 0 <= nx <= 3 and 0 <= ny <= 3:
                    nr = route + direction
                    yield (1, (nr, md5digest(data + nr), nx, ny))

    rv = a_star_solve(
        origin=('', md5digest(data), 0, 0),
        is_target=lambda state: state[2] == 3 and state[3] == 3,
        neighbours=neighbours,
        heuristic=lambda node, *dummy: abs(node[2] - 3 + abs(node[3] - 3)),
        find_all=find_max_length)

    if not find_max_length:
        return rv[1][0]
    else:
        return max(rv)[0]


def part1():
    print('answer', solve(d.data))


def part2():
    print('answer', solve(d.data, find_max_length=True))

