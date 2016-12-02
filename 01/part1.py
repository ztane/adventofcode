dirs = [(0, 1),
        (1, 0),
        (0, -1),
        (-1, 0)]

current_dir = 0
current_coord = (0, 0)

for i in input_file().split(', '):
    lr = i[0]
    amt = int(i[1:])
    current_dir = (current_dir + [1, -1][lr == 'L']) % 4
    delta = dirs[current_dir]
    current_coord = current_coord[0] + amt * delta[0], current_coord[1] + amt * delta[1]

print(abs(current_coord[0]) + abs(current_coord[1]))
