from hashlib import md5
from itertools import count
import re

from helpers import get_aoc_data, defaultdict, md5digest

start = get_aoc_data(day=14).data

hexes = 'abcdef0123456789'
has_triple = re.compile('|'.join(i * 3 for i in hexes))
has_5 = re.compile('|'.join(i * 5 for i in hexes))


def hashes_part1():
    hasher = (start + '%d').encode()
    for i in count():
        yield i, md5digest(hasher % i)


def hashes_part2():
    hasher = (start + '%d').encode()
    for i in count():
        current_hash = md5digest(hasher % i)
        for _ in range(2016):
            current_hash = md5digest(current_hash)

        yield i, current_hash


def find_64th(gen):
    need5 = defaultdict(list)
    hash_indexes = []
    upper_limit = 2 ** 31
    for i, current_hash in gen:
        if i > upper_limit:
            break

        m3 = has_triple.search(current_hash)
        m5 = has_5.search(current_hash)
        if m5:
            triple = m5.group(0)[:3]
            candidate_indexes = need5.pop(triple)
            for j in candidate_indexes:
                if i - j <= 1000:
                    hash_indexes.append(j)
                    if len(hash_indexes) == 64:
                        upper_limit = max(hash_indexes) + 1000
                        print('found key #{}'.format(len(hash_indexes)))
                        print('hashing 1000 more to ensure completion')

            print('found key #{}'.format(len(hash_indexes)), end='\r')

        if m3:
            marker = m3.group(0)
            need5[marker].append(i)

    return sorted(hash_indexes)[63]


def part1():
    print('The key is', find_64th(hashes_part1()))


def part2():
    print('The key is', find_64th(hashes_part2()))

