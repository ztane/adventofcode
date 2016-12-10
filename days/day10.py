from helpers import *
import re


d = get_aoc_data(day=10)
bot_output = re.compile(r'bot (\d+) gives low to (output|bot) (\d+)'
                        r' and high to (output|bot) (\d+)')

part2_value = None


def part1():
    global part2_value
    connections = OrderedDict()
    thingies = {
        'bot': defaultdict(list),
        'output': defaultdict(list),
    }
    bot, output = items(thingies, 'bot', 'output')

    for i in d.lines():
        if i.startswith('value'):
            v, bot_no = get_ints(i)
            bot[bot_no].append(v)

        else:
            m = bot_output.match(i)

            bot_no, ltype, lno, htype, hno = m.groups()
            connections[int(bot_no)] = (
                thingies[ltype][int(lno)],
                thingies[htype][int(hno)]
            )

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