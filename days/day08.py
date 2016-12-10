import numpy as np
from helpers import chained, get_ints, draw_display, get_aoc_data, Parser
import time
from PIL import Image

d = get_aoc_data(day=8)

display = np.zeros((6, 50), dtype=np.uint8)

rotate_row = Parser('rotate row y=<int> by <int>')
rotate_col = Parser('rotate column x=<int> by <int>')
rect = Parser('rect <int>x<int>')


def part1():
    for i in d.lines:
        if rect(i):
            x, y = rect
            display[:y, :x] = 1
        elif rotate_col(i):
            x, by = rotate_col
            display[:, x] = np.roll(display[:, x], by)
        elif rotate_row(i):
            y, by = rotate_row
            display[y, :] = np.roll(display[y, :], by)
        else:
            print('Unknown', i)

        print('\033[2J\033[H' + i)
        draw_display(display)
        # time.sleep(0.1)

    im = Image.fromarray(display * 250)
    im.save('your_file.png')

    print('Number of pixels set:', sum(chained(display)))


def part2():
    print('Read the answer yourself ^')




