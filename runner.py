#!/usr/bin/env python3

import sys
if sys.version_info < (3,):
    print('WTF, are you running my code in Python 2??!')
    sys.exit(1)

from os import path
import helpers

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: runner.py daynumber')
        sys.exit(2)

    day = int(sys.argv[1])
    day_module = 'day{:02}'.format(day)
    module = getattr(__import__('days.' + day_module), day_module)
    for part in [1, 2]:
        func = getattr(module, 'part{}'.format(part), None)
        if func:
            print('Day {} part {}'.format(day, part))
            func()
        else:
            print('Day {}; no part {}'.format(day, part))
