from helpers import get_aoc_data, clamp

d = get_aoc_data(day=2)

directions = {
    'U': (0, -1),
    'D': (0,  1),
    'L': (-1, 0),
    'R': (1,  0)
}


def part1():
    keyboard = """
       123
       456
       789
    """.split()
    
    x, y = 1, 1

    seq = ''
    
    for line in d.lines:
        for i in line:
            dx, dy = directions[i]
            x = clamp(x + dx, 0, 2)
            y = clamp(y + dy, 0, 2)
    
        seq += str(keyboard[y][x])
    
    print(seq)


def part2():
    keyboard = """
        xx1xx
        x234x
        56789
        xABCx
        xxDxx
    """.split()
    
    x, y = 2, 2
    seq = ''
    
    for line in d.lines:
        for i in line:
            dx, dy = directions[i]
            new_x = clamp(x + dx, 0, 4)
            new_y = clamp(y + dy, 0, 4)
            if keyboard[new_y][new_x] != 'x':
                x, y = new_x, new_y
    
        seq += keyboard[y][x]
    
    print(seq)
