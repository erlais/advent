import logging
from copy import copy

from intcode import Program


def grid_to_str(grid):
    res = ''
    for row in grid:
        res += '\n'
        for col in row:
            res += str(col)
    return res


def make_grid(side_len, def_val=0):
    """ makes a square grid[y][x] """
    grid = []
    for row in range(side_len):
        grid.append([])
        for _ in range(side_len):
            grid[row].append(def_val)
    return grid


def count_adj(grid, y, x):
    try:
        count = 0
        if grid[y-1][x] == '#':
            count += 1
        if grid[y+1][x] == '#':
            count += 1
        if grid[y][x-1] == '#':
            count += 1
        if grid[y][x+1] == '#':
            count += 1
    except IndexError:
        return 1
    return count

def main_part1(program):
    frame = []

    for out in program.runner():
        if out is None:
            break
        frame.append(out)

    frame_str = ''
    for pixel in frame:
        frame_str += chr(pixel)

    grid = []
    for line in frame_str.split('\n'):
        grid.append([char for char in line])

    print(grid_to_str(grid))

    part1 = []
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col != '#':
                continue
            n_adj = count_adj(grid, y, x)
            # print(n_adj)
            if n_adj > 2:
                part1.append(y * x)

    print(len(part1))  # number of intersections
    print(sum(part1))  # answer

def main_part2(program):
    """
    L10, R8, R8,
    L10, R8, R8,
    L10, L12, R8, R10,
    R10, L12, R10,
    L10, L12, R8, R10,
    R10, L12, R10,
    L10, L12, R8, R10,
    R10, L12, R10,
    R10, L12, R10,
    L10, R8, R8

    main:
    A,A,B,C,B,C,B,C,C,A

    patterns:
    A: L10, R8, R8
    B: L10, L12, R8, R10
    C: R10, L12, R10
    """
    main_routine = 'A,A,B,C,B,C,B,C,C,A\n'

    funcA = 'L,10,R,8,R,8\n'
    funcB = 'L,10,L,12,R,8,R,10\n'
    funcC = 'R,10,L,12,R,10\n'
    debug = 'n\n'

    input_str = main_routine + funcA + funcB + funcC + debug
    input_list = list(map(ord, input_str))
    print(input_list)

    program.in_val_list.extend(input_list)
    for out in program.runner():
        if out is None:
            break
        if out < 128:
            print(chr(out), end='')
        else:
            print(out)


if __name__ == "__main__":
    ll = logging.WARNING
    logging.basicConfig(format='%(message)s', level=ll)

    # INIT
    data = open('input17').read().strip().split(',')
    data = [int(x) for x in data]
    extra_mem = [0 for _ in range(10000)]
    data = data + extra_mem

    # RUN part1
    # prog = Program(data, 'Day17p1')
    # main_part1(prog)

    # RUN part2
    data[0] = 2
    prog = Program(data, 'Day17p2')
    main_part2(prog)
