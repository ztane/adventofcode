import helpers
import sys
from os import path

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: runner.py daynumber')
        sys.exit(2)

    day = int(sys.argv[1])
    day_directory = path.join(path.dirname(__file__), '{:02}'.format(day))

    for part in [1, 2]:
        with open(path.join(day_directory, 'part{}.py'.format(part))) as f:
            helpers._set_input(path.join(day_directory, 'input.txt'))
            code = f.read()
            print('Day {} part {}'.format(day, part))
            exec(code, dict(helpers.__dict__))

