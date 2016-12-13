from helpers import *

d = get_aoc_data(day=12)

print(d.data)
cpy = Parser('cpy <> <>')
inc = Parser('inc <>')
dec = Parser('dec <>')
jnz = Parser('jnz <> <int>')

memory = []
registers = {}
ip = 0


def accessor(operand):
    if operand.isalpha():
        return lambda: registers[operand]
    else:
        val = int(operand)
        return lambda: val


for i in d.lines:
    if cpy(i):
        src, tgt = cpy

        @memory.append
        def instr(src=accessor(src), tgt=tgt):
            registers[tgt] = src()

    elif inc(i):
        tgt, = inc

        @memory.append
        def instr(tgt=tgt):
            registers[tgt] += 1

    elif dec(i):
        tgt, = dec

        @memory.append
        def instr(tgt=tgt):
            registers[tgt] -= 1

    elif jnz(i):
        op, branch = jnz

        @memory.append
        def instr(op=accessor(op), branch=branch):
            global ip
            if op():
                ip += branch - 1

    else:
        print('failing instruction', i)
        exit(1)



@memory.append
def hlt():
    print('Completed. a={}'.format(registers['a']))
    return True


def run():
    global ip
    ctr = 0
    while not memory[ip]():
        ip += 1
        ctr += 1
    print(ctr, 'clock cycles')


def part1():
    global ip
    ip = 0
    registers.update(dict.fromkeys('abcd', 0))
    run()


def part2():
    global ip
    ip = 0

    registers.update(dict.fromkeys('abcd', 0))
    registers['c'] = 1
    run()
