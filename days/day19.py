from collections import deque

from helpers import get_aoc_data

d = get_aoc_data(day=19)


def solve_part1(n_elves):
    elves = deque(range(1, n_elves + 1))

    while len(elves) > 1:
        e = elves.popleft()
        elves.popleft()
        elves.append(e)

    return elves[0]


def solve_part2(n_elves):
    elves = list(range(1, n_elves + 1))
    elves_remaining = n_elves
    on_left = deque()
    on_right = deque()
    on_left.extend(elves[:len(elves) // 2])
    on_right.extend(elves[len(elves) // 2:][::-1])

    while True:
        if not on_left:
            on_left.append(on_right.pop())

        current_elf = on_left.popleft()
        elves_remaining -= 1

        # balance the sides
        if elves_remaining % 2:
            tgt = elves_remaining // 2 + 1
        else:
            tgt = elves_remaining

        while len(on_left) > tgt:
            on_right.append(on_left.pop())

        while len(on_right) > len(on_left):
            on_left.append(on_right.pop())

        # eliminate the elf on the left or just opposite
        on_left.pop()

        # and replace the current_elf to the right side of the next one
        on_right.appendleft(current_elf)
        if elves_remaining == 1:
            return current_elf


assert solve_part1(5) == 3
assert solve_part2(5) == 2


def part1():
    print('answer is', solve_part1(int(d.data)))


def part2():
    print('answer is', solve_part2(int(d.data)))
