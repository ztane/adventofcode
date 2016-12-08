from helpers import get_aoc_data

d = get_aoc_data(day=1)

dirs = [(0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)]


def part1():
    current_dir = 0
    x, y = 0, 0

    for i in d.split():
        lr = i[0]
        amt = int(i[1:])
        current_dir = (current_dir + [1, -1][lr == 'L']) % 4
        dx, dy = dirs[current_dir]
        x += amt * dx
        y += amt * dy

    print(abs(x) + abs(y))


def part2():
    current_dir = 0
    x, y = 0, 0

    seen = {(0, 0)}

    for i in d.split():
        lr = i[0]
        amt = int(i[1:])
        current_dir = (current_dir + [1, -1][lr == 'L']) % 4
        dx, dy = dirs[current_dir]
        for _ in range(amt):
            x, y = x + dx, y + dy
            if (x, y) in seen:
                print(abs(x) + abs(y))
                return

            seen.add((x, y))
