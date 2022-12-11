from copy import deepcopy
from pprint import pprint

data = '''\
#####
.#.##
#...#
..###
#.##.'''

def get_adj(y, x):
    return [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

def bio(g):
    n = 0
    total = 0
    for row in g:
        for col in row:
            if col == '#':
                total += 2**(n)
            n += 1
    return total

def tick(g):
    new_g = deepcopy(g)
    for y, row in enumerate(g):
        for x, col in enumerate(row):
            adjacent = get_adj(y, x)
            count_bugs = 0
            for adj_y, adj_x in adjacent:
                if 0 <= adj_y < len(g) and 0 <= adj_x < len(g[0]):
                    if g[adj_y][adj_x] == '#':
                        count_bugs += 1
            if g[y][x] == '#' and count_bugs != 1:
                new_g[y][x] = '.'
            elif g[y][x] == '.' and count_bugs in (1, 2):
                new_g[y][x] = '#'
    return new_g


grid = [[c for c in col] for col in data.splitlines()]
seen = []
while True:
    if grid in seen:
        break
    seen.append(grid)
    new_grid = tick(grid)
    grid = new_grid

print(bio(grid))
