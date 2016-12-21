from helpers import *

d = get_aoc_data(day=21)

swap_pos = Parser('swap position <int> with position <int>')
swap_let = Parser('swap letter <str> with letter <str>')
reverse_pos = Parser('reverse positions <int> through <int>')
rotate_left = Parser('rotate left <int> step<>')
rotate_right = Parser('rotate right <int> step<>')
move_pos = Parser('move position <int> to position <int>')
rotate_pos = Parser('rotate based on position of letter <>')


def solve(lines, unscrambled):
    current = list(unscrambled)
    for l in lines:
        if swap_pos(l):
            a, b = swap_pos
            current[a], current[b] = current[b], current[a]

        elif swap_let(l):
            a, b = swap_let
            a = current.index(a)
            b = current.index(b)
            current[a], current[b] = current[b], current[a]

        elif reverse_pos(l):
            a, b = reverse_pos
            current[a:b + 1] = current[a:b + 1][::-1]

        elif rotate_left(l):
            shift, _ = rotate_left
            current = current[shift:] + current[:shift]

        elif rotate_right(l):
            shift, _ = rotate_right
            if shift:
                current = current[-shift:] + current[:-shift]

        elif move_pos(l):
            a, b = move_pos
            c = current.pop(a)
            current[b:b] = [c]

        elif rotate_pos(l):
            a, = rotate_pos
            idx = current.index(a)
            current = current[-1:] + current[:-1]
            if idx:
                current = current[-idx:] + current[:-idx]
            if idx >= 4:
                current = current[-1:] + current[:-1]

        else:
            print('unknown command', l)

    return ''.join(current)


def part1():
    print('answer is', solve(d.lines, 'abcdefgh'))


def part2():
    p = list(permutations('fbgdceah'))
    print('Attempting to crack the password,', len(p), 'permutations')
    for n, i in enumerate(p):
        if not n % 1000:
            print('\rtried {:.2f} %... '.format(n / len(p) * 100), end='')

        if solve(d.lines, i) == 'fbgdceah':
            print('\rtried {:.2f} %... '.format(n / len(p) * 100), end='')
            print(' CRACKED!!!\nAnswer is ', ''.join(i))
            break
