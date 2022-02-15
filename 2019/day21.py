import logging
from copy import copy
from collections import deque

from intcode import Program


def main(program):
    """
    123456789
    ABCDEFGHI
    """
    # Part 1: jump if
    sc =  'NOT A J\n'  # a is hole
    sc += 'NOT B T\n'
    sc += 'OR T J\n'   # or b is hole
    sc += 'NOT C T\n'
    sc += 'OR T J\n'   # or c is hole
    sc += 'AND D J\n'  # and d is safe

    # Part 2: Do previous, but only if we can jump again straight away or keep walking
    sc += 'NOT E T\n'  # E (next after landing) is hole
    sc += 'AND H T\n'  # ... but H is safe
    sc += 'OR E T\n'   # E is walkable
    sc += 'AND T J\n'  # D is safe to land AND (E is walkable OR E and H are safe)
    sc += 'RUN\n'
    program.in_val_list = deque(map(ord, sc))
    for out in program.runner():
        if out is None:
            break
        if out > 128:
            print(out)
        else:
            print(chr(out), end='')

if __name__ == "__main__":
    ll = logging.WARNING
    logging.basicConfig(format='%(message)s', level=ll)

    # INIT
    data = open('input21').read().strip().split(',')
    data = [int(x) for x in data]
    extra_mem = [0 for _ in range(10000)]
    data = data + extra_mem

    # RUN part1
    prog = Program(data, 'Day21')
    main(prog)
