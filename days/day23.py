from helpers import *

d = get_aoc_data(day=23)

cpy = Parser('cpy <> <>')
inc = Parser('inc <>')
dec = Parser('dec <>')
multiply = Parser('multiply <> <> <>')
jnz = Parser('jnz <> <>')
toggle = Parser('tgl <>')

print('Doing the peephole optimization')
d.data = d.data.replace("""\
cpy b c
inc a
dec c
jnz c -2
dec d
jnz d -5""",

"""\
multiply b d a
cpy 0 d
jnz 0 0
jnz 0 0
jnz 0 0
jnz 0 0""")

registers = {}
ip = 0
toggled_instructions = defaultdict(bool)


def accessor(operand):
    if operand.isalpha():
        return lambda: registers[operand]
    else:
        val = int(operand)
        return lambda: val


def parse_code(lines):
    memory = []
    for i in lines:
        if cpy(i):
            src, tgt = cpy

            @memory.append
            def instr(src=accessor(src), tgt=tgt):
                registers[tgt] = src()

        elif multiply(i):
            a, b, c = multiply

            @memory.append
            def instr(a=a, b=b, c=c):
                registers[c] += registers[a] * registers[b]

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
            def instr(op=accessor(op), branch=accessor(branch)):
                global ip
                if op():
                    ip += branch() - 1

        elif toggle(i):
            instr_no, = toggle

            @memory.append
            def instr(op=accessor(instr_no)):
                instr_no = op()
                instr_no += ip
                toggled_instructions[instr_no] = not toggled_instructions[instr_no]

        else:
            print('failing instruction', i)
            exit(1)

    @memory.append
    def hlt():
        print('Completed. a={}'.format(registers['a']))
        return True

    return memory


def toggled(code):
    def replace(m):
        return {
            'inc': 'dec',
            'dec': 'inc',
            'tgl': 'inc',
            'jnz': 'cpy',
            'cpy': 'jnz'
        }[m.group(0)]

    return re.sub('inc|dec|cpy|tgl|jnz', replace, code)


memory = parse_code(d.lines)
toggled_memory = parse_code(toggled(d.data).splitlines())


def run():
    global ip
    ctr = 0
    while True:
        if toggled_instructions[ip]:
            try:
                state = toggled_memory[ip]()
            except Exception as e:
                print(str(e), repr(e))
        else:
            state = memory[ip]()

        if state:
            break

        ip += 1
        ctr += 1

    print(ctr, 'clock cycles')


def part1():
    global ip
    ip = 0
    registers.update(dict.fromkeys('abcd', 0))
    toggled_instructions.clear()
    registers['a'] = 7
    run()


def part2():
    global ip
    ip = 0

    toggled_instructions.clear()
    registers.update(dict.fromkeys('abcd', 0))
    registers['a'] = 12
    run()
