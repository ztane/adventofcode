keyboard = """
    xx1xx
    x234x
    56789
    xABCx
    xxDxx
""".split()

x, y = 2, 2
directions = {
    'U': (0, -1),
    'D': (0,  1),
    'L': (-1, 0),
    'R': (1,  0)
}

seq = ''

for line in input_lines():
    for i in line:
        dx, dy = directions[i]
        new_x = clamp(x + dx, 0, 4)
        new_y = clamp(y + dy, 0, 4)
        if keyboard[new_y][new_x] != 'x':
            x, y = new_x, new_y

    seq += keyboard[y][x]

print(seq)
