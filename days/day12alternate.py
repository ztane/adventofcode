from helpers import *

d = get_aoc_data(day=12)

cpy = Parser('cpy <> <>')
inc = Parser('inc <>')
dec = Parser('dec <>')
jnz = Parser('jnz <> <int>')

instructions = []


for i in d.lines:
    if cpy(i):
        instructions.append('{1} = {0}'.format(*cpy))

    elif inc(i):
        instructions.append('{0} += 1'.format(*inc))

    elif dec(i):
        instructions.append('{0} -= 1'.format(*dec))

    elif jnz(i):
        instructions.append('ip += {1} - 1 if {0} else 0'.format(*jnz))

    else:
        print('failing instruction', i)
        exit(1)

instructions.append('print("Finished. a = {}".format(a)); raise SystemExit()')
instructions = [compile(c, '<instruction>', 'exec') for c in instructions]


def run(registers):
    registers['__builtins__'] = globals()['__builtins__']
    while True:
        try:
            exec(instructions[registers['ip']], registers)
            registers['ip'] += 1
        except SystemExit:
            break


def part1():
    registers = dict.fromkeys('abcd', 0)
    registers['ip'] = 0

    run(registers)


def part2():
    registers = dict.fromkeys('abcd')
    registers['ip'] = 0
    registers['c'] = 1

    run(registers)
