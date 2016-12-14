from helpers import *

start = get_aoc_data(day=14).data

hexes = 'abcdef0123456789'
has_triple = re.compile('|'.join(i * 3 for i in hexes))
has_5 = re.compile('|'.join(i * 5 for i in hexes))


def hashes_part1():
    hasher = (start + '%d').encode()
    for i in count():
        yield i, md5(hasher % i).hexdigest()


def hashes_part2():
    hasher = (start + '%d').encode()
    for i in count():
        current_hash = md5(hasher % i).hexdigest()
        for _ in range(2016):
            current_hash = md5(current_hash.encode()).hexdigest()

        yield i, current_hash


def find_64th(gen):
    need5 = defaultdict(list)
    hash_count = 0
    for i, current_hash in gen:
        m3 = has_triple.search(current_hash)
        m5 = has_5.search(current_hash)
        if m5:
            triple = m5.group(0)[:3]
            threekeys = need5[triple]
            for j in list(threekeys):
                if i - j <= 1000:
                    hash_count += 1
                    if hash_count == 64:
                        print('found key #{}'.format(hash_count))
                        return j

            del threekeys[:]
            print('found key #{}'.format(hash_count), end='\r')

        if m3:
            marker = m3.group(0)
            need5[marker].append(i)


def part1():
    print('The key is', find_64th(hashes_part1()))


def part2():
    print('The key is', find_64th(hashes_part2()))

