import operator as op
from collections import OrderedDict
from collections import defaultdict
from functools import reduce
from helpers import get_aoc_data, Parser, items

d = get_aoc_data(day=10)
part2_value = None

value = Parser('value <int> goes to bot <int>')
gives = Parser('bot <int> gives low to <str:output|bot> <int>'
               ' and high to <str:output|bot> <int>')


def part1():
    global part2_value
    connections = OrderedDict()
    thingies = {
        'bot': defaultdict(list),
        'output': defaultdict(list),
    }
    bot, output = items(thingies, 'bot', 'output')

    for i in d.lines():
        if value(i):
            v, bot_no = value
            bot[bot_no].append(v)

        elif gives(i):
            bot_no, ltype, lno, htype, hno = gives
            connections[bot_no] = (
                thingies[ltype][lno],
                thingies[htype][hno]
            )
        else:
            raise ValueError("Input doesn't match:", i)

    while True:
        for k, v in bot.items():
            assert len(v) <= 2
            if len(v) == 2:
                low_conn, high_conn = connections[k]
                low_value, high_value = sorted(v)
                del v[:]
                low_conn.append(low_value)
                high_conn.append(high_value)

                if (low_value, high_value) == (17, 61):
                    print(k)

                # break the for loop as we've changed the dictionary
                break
        else:
            part2_value = reduce(op.mul, sum(items(output, 0, 1, 2), []))
            return


def part2():
    print(part2_value)