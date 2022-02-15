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

def part1(data):
    grid = [['.' for y in range(50)] for x in range(50)]
    input_list = []
    for x in range(50):
        for y in range(50):
            input_list.append([x, y])

    count = 0
    for coords in input_list:
        prog = Program(copy(data), 'Day19p1')
        prog.in_val_list.extend(coords)

        for out in prog.runner():
            if out is None:
                break
            if out == 1:
                grid[coords[1]][coords[0]] = '#'
                count += 1
    print(grid_to_str(grid))
    print(count)

def part2(data):
    x = 0
    y = 0
    running = True
    while running:
        prog = Program(copy(data), 'Day19p2')
        prog.in_val_list.extend([x, y])
        for out in prog.runner():
            if out is None:
                break
            if out == 1:
                p2 = Program(copy(data))
                p2.in_val_list.extend([x+99, y-99])
                pg = p2.runner()
                check = next(pg)
                if check == 1:
                    closest_point = (x, y-99)
                    running = False
                break
            x += 1
        y += 1

    res = closest_point[0] * 10000 + closest_point[1]
    print(res)


if __name__ == "__main__":
    ll = logging.WARNING
    logging.basicConfig(format='%(message)s', level=ll)

    # INIT
    data = open('input19').read().strip().split(',')
    data = [int(x) for x in data]
    extra_mem = [0 for _ in range(10000)]
    data = data + extra_mem

    # RUN
    part1(data)
    part2(data)
