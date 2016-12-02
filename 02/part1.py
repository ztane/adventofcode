keyboard = """
   123
   456
   789
""".split()

x, y = 1, 1
directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}

seq = ''

for line in input_lines():
    for i in line:
        dx, dy = directions[i]
        x = clamp(x + dx, 0, 2)
        y = clamp(y + dy, 0, 2)

    seq += str(keyboard[y][x])

print(seq)
