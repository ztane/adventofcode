from helpers import *
from hashlib import md5

d = get_aoc_data(day=5)


def part1():
    door_id = (d.data.strip() + '%d').encode()
    password = ''
    for i in count():
        digest = md5(door_id % i).hexdigest()

        if digest.startswith('00000'):
            password += digest[5]
            print('Solved character #{}: position {} is {}'
                  .format(len(password), len(password) - 1, digest[5]))

            if len(password) == 8:
                break

    print(password)


def part2():
    door_id = (d.data.strip() + '%d').encode()
    positions = {}
    for i in count():
        digest = md5(door_id % i).hexdigest()

        if digest.startswith('00000'):
            pos = digest[5]
            if pos < '8' and pos not in positions:
                password_char = digest[6]
                positions[pos] = password_char
                pw_length = len(positions)
                print('Solved character #{}: position {} is {}'
                      .format(pw_length, pos, password_char))

            if len(positions) == 8:
                break

    print(''.join([i[1] for i in sorted(positions.items())]))
