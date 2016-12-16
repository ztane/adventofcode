from helpers import *

d = get_aoc_data(day=16)


t01 = str.maketrans('01', '10')


def make_dragon(a):
    b = a.translate(t01)
    return a + '0' + b[::-1]


assert make_dragon('0') == '001'
assert make_dragon('1') == '100'
assert make_dragon('111100001010') == '1111000010100101011110000'


cksum_2 = {'01': '0', '10': '0', '11': '1', '00': '1'}


def checksum(a):
    while not len(a) & 1:
        a = re.sub('..', lambda r: cksum_2[r.group(0)], a)

    return a


def solve(data, length):
    a = data
    while len(a) < length:
        a = make_dragon(a)

    c = checksum(a[:length])
    return c


def part1():
    print('answer', solve(d.data, 272))


def part2():
    print('answer', solve(d.data, 35651584))
