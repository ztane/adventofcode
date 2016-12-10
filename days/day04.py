from collections import Counter
from string import ascii_lowercase

import re

from helpers import get_aoc_data, Parser

d = get_aoc_data(day=4)

ascii_l = ascii_lowercase
tables = [str.maketrans(ascii_l, ascii_l[i:] + ascii_l[:i]) for i in range(26)]
room_parser = Parser('<str:[a-z-]+><int>[<>]')


def decrypt(name, sector):
    table_no = sector % 26
    return name.translate(tables[table_no])


def calculate_checksum(room_id):
    counts = Counter(room_id.replace('-', ''))
    return ''.join(i[0]
                   for i in
                   sorted(counts.items(), key=lambda x: (-x[1], x[0])))[:5]


def part1():
    sector_sum = 0
    for room_id, sector, checksum in room_parser.for_lines(d.lines):
        if calculate_checksum(room_id) == checksum:
            sector_sum += int(sector)

    print(sector_sum)


def part2():
    for room_id, sector, checksum in room_parser.for_lines(d.lines):
        if calculate_checksum(room_id.replace('-', '')) == checksum:
            room_id = decrypt(room_id.replace('-', ' ').strip(), sector)
            if 'north' in room_id and 'pole' in room_id  and 'object' in room_id:
                print(room_id, 'is room number', sector)
                return
