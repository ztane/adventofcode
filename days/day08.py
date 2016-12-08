from helpers import *
import numpy as np

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

        print(i)
        draw_display(display)

    print('Number of pixels set:', sum(chain.from_iterable(display)))


def part2():
    print('Read the answer yourself')
    draw_display(display)
