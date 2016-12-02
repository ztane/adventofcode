dirs = [(0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)]

current_dir = 0
x, y = 0, 0

seen = {(0, 0)}

for i in input_split():
    lr = i[0]
    amt = int(i[1:])
    current_dir = (current_dir + [1, -1][lr == 'L']) % 4
    dx, dy = dirs[current_dir]
    for _ in range(amt):
        x, y = x + dx, y + dy
        if (x, y) in seen:
            print(abs(x) + abs(y))
            break

        seen.add((x, y))

    else:
        continue

    break
