import numpy as np
from helpers import chained, get_ints, draw_display, get_aoc_data
import time

d = get_aoc_data(day=8)

display = np.zeros((6, 50), dtype=int)


def part1():
    for i in d.lines():
        if i.startswith('rect'):
            x, y = get_ints(i)
            display[:y, :x] = 1
        elif i.startswith('rotate column'):
            x, by = get_ints(i)
            display[:, x] = np.roll(display[:, x], by)
        elif i.startswith('rotate row'):
            y, by = get_ints(i)
            display[y, :] = np.roll(display[y, :], by)
        else:
            print('Unknown', i)

        print('\033[2J\033[H' + i)
        draw_display(display)
        time.sleep(0.1)

    print('Number of pixels set:', sum(chained(display)))


def part2():
    print('Read the answer yourself ^')
