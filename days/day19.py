from collections import deque

from helpers import get_aoc_data

d = get_aoc_data(day=19)


def solve_part1_proper(n_elves):
    """
    Solve the part 1 problem for n elves
    :param n_elves: the number of elves
    :return: the remaining one
    """
    elves = deque(range(1, n_elves + 1))
    popleft = elves.popleft
    append = elves.append
    # piece of cake
    current_elf = None
    while elves:
        # move one on the other side
        current_elf = popleft()
        append(current_elf)
        # and eliminate the next one
        popleft()

    return current_elf


def solve_part1(n):
    """
    Use the trick from http://gurmeet.net/puzzles/josephus-problem/index.html
    :param n: number of elves
    :return: the remaining one
    """
    s = format(n, 'b')
    return int(s[1:] + s[0], 2)


def solve_part2(n_elves):
    """
    Solve the part 2 problem for n elves
    :param n_elves: the number of elves
    :return: the remaining one
    """

    elves = range(1, n_elves + 1)
    on_left = deque()
    on_right = deque()

    # I am **ignoring** the left/right distinction on the deque. I really do not
    # think deque as left-right; instead I always think append/pop operating on
    # the end of it, and `*left` doing the opposite.
    #
    # Thus instead instead the "left" in either queue means now **closest** to
    # the current elf; and the "right" is furthest away - that is, deque indices
    # grow as we move further from the current elf.
    on_left.extend(elves[:len(elves) // 2])
    on_right.extendleft(elves[len(elves) // 2:])

    on_left_append_far = on_left.append
    on_left_pop_near = on_left.popleft
    on_left_pop_far = on_left.pop
    on_right_append_far = on_right.append
    on_right_append_near = on_right.appendleft
    on_right_pop_near = on_right.popleft
    on_right_pop_far = on_right.pop

    while True:
        # sometimes the left queue is empty and both are on the right side;
        # then pull the elf on the furthest of right side and pop it to the left
        if not on_left:
            on_left_append_far(on_right_pop_far())

        # remove the current elf from queues. Always the next one from left
        current_elf = on_left_pop_near()
        n_elves -= 1

        # balance the sides so that left side has one more elf
        if n_elves % 2:
            tgt = n_elves // 2 + 1
        else:
            tgt = n_elves

        while len(on_left) > tgt:
            on_right_append_far(on_left_pop_far())

        while len(on_right) > len(on_left):
            on_left_append_far(on_right_pop_far())

        # eliminate the elf on the left or just opposite
        on_left_pop_far()

        if n_elves == 1:
            return current_elf

        # otherwise move the current_elf to the right side of the next one
        on_right_append_near(current_elf)


assert solve_part1(5) == 3
assert solve_part2(5) == 2


def part1():
    print('answer is', solve_part1(int(d.data)))


def part2():
    print('answer is', solve_part2(int(d.data)))
