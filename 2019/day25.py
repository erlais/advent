import logging
from collections import deque
from itertools import combinations

from intcode import Program


def drop_all(equipped):
    res = []
    for itm in equipped:
        res.extend([ord(c) for c in 'drop '])
        res.extend([ord(c) for c in itm])
        res.append(10)
    return res

def try_combs(combs):
    res = []
    for cmb in combs:
        for itm in cmb:
            res.extend([ord(c) for c in 'take '])
            res.extend([ord(c) for c in itm])
            res.append(10)
        res.extend([ord(c) for c in 'east'])
        res.append(10)
        res.extend(drop_all(cmb))
    return res

def main(program):
    # after moves, next move to east is pressure room (8 items)
    moves = ['north', 'take mouse', 'north', 'take pointer', 'south', 'south',  # north branch
            'west', 'take monolith', 'north', 'west', 'take food ration', 'south', 'take space law space brochure', 'north', 'east', 'south', 'south', 'take sand', 'south', 'west', 'take asterisk', 'south', 'take mutex', 'north', 'east', 'north', 'north', 'east',  # west branch
            'south', 'south', 'west', 'south', 'inv']  # south branch

    items = ['mouse', 'pointer', 'monolith', 'food ration', 'space law space brochure', 'sand', 'asterisk', 'mutex']

    initial_moves = []
    for move in moves:
        for ch in move:
            initial_moves.append(ord(ch))
        initial_moves.append(10)

    program.in_val_list.extend(initial_moves)
    program.in_val_list.extend(drop_all(items))
    program.in_val_list.extend(try_combs(combinations(items, 4)))
    for out in program.runner():
        if out is None:
            break
        if out > 128:
            print(out)
        else:
            print(chr(out), end='')
            # if chr(out) == '?':
            #     user_in = input(' ')
            #     cmd = user_in + '\n'
            #     program.in_val_list.extend(list(map(ord, cmd)))

if __name__ == "__main__":
    ll = logging.WARNING
    logging.basicConfig(format='%(message)s', level=ll)

    # INIT
    data = open('input25').read().strip().split(',')
    data = [int(x) for x in data]
    extra_mem = [0 for _ in range(10000)]
    data = data + extra_mem

    # RUN part1
    prog = Program(data, 'Day25')
    main(prog)
