from copy import deepcopy
from pprint import pprint

data = '''\
#####
.#.##
#...#
..###
#.##.'''

def get_adj(lvl, y, x):
    g = levels[lvl]
    res = []
    # INWARDS
    if y == 1 and x == 2:    # top of middle
        res.extend([g[0][x], g[y][1], g[y][3]])
        res.extend(levels[lvl+1][0])
    elif y == 3 and x == 2:  # bottom of middle
        res.extend([g[4][x], g[y][1], g[y][3]])
        res.extend(levels[lvl+1][4])
    elif y == 2 and x == 1:  # left of middle
        res.extend([g[y][0], g[1][x], g[3][x]])
        res.extend([row[0] for row in levels[lvl+1]])
    elif y == 2 and x == 3:  # right of middle
        res.extend([g[y][4], g[1][x], g[3][x]])
        res.extend([row[4] for row in levels[lvl+1]])
    # OUTWARDS
    elif y == 0 and x == 0:  # upper left corner
        res.extend([g[y][1], g[1][x]])
        res.append(levels[lvl-1][1][2])
        res.append(levels[lvl-1][2][1])
    elif y == 4 and x == 0:  # lower left corner
        res.extend([g[y][1], g[3][x]])
        res.append(levels[lvl-1][3][2])
        res.append(levels[lvl-1][2][1])
    elif y == 0 and x == 4:  # upper right corner
        res.extend([g[y][3], g[1][x]])
        res.append(levels[lvl-1][1][2])
        res.append(levels[lvl-1][2][3])
    elif y == 4 and x == 4:  # lower right corner
        res.extend([g[y][3], g[3][x]])
        res.append(levels[lvl-1][3][2])
        res.append(levels[lvl-1][2][3])
    elif y == 0 and x in (1, 2, 3):  # upper mid
        res.extend([g[y][x-1], g[y][x+1], g[y+1][x]])
        res.append(levels[lvl-1][1][2])
    elif y == 4 and x in (1, 2, 3):  # lower mid
        res.extend([g[y][x-1], g[y][x+1], g[y-1][x]])
        res.append(levels[lvl-1][3][2])
    elif x == 0 and y in (1, 2, 3):  # left mid
        res.extend([g[y-1][x], g[y+1][x], g[y][x+1]])
        res.append(levels[lvl-1][2][1])
    elif x == 4 and y in (1, 2, 3):  # right mid
        res.extend([g[y-1][x], g[y+1][x], g[y][x-1]])
        res.append(levels[lvl-1][2][3])
    else:  # other cases
        res.extend([g[y-1][x], g[y+1][x], g[y][x-1], g[y][x+1]])

    return res

def tick(g, lvl):
    new_g = deepcopy(g)
    for y, row in enumerate(g):
        for x, col in enumerate(row):
            if x == 2 and y == 2:  # middle square doesn't exist in part2
                continue
            adjacent = get_adj(lvl, y, x)
            count_bugs = adjacent.count('#')
            if g[y][x] == '#' and count_bugs != 1:
                new_g[y][x] = '.'
            elif g[y][x] == '.' and count_bugs in (1, 2):
                new_g[y][x] = '#'
    return new_g


# Initialize
num_levels = 200
grid = [[c for c in col] for col in data.splitlines()]
empty_grid = [['.' for _ in range(5)] for _ in range(5)]
levels = {i: empty_grid for i in range(-101, 102)}  # add one level either side as buffer
levels[0] = grid

# Run
for _ in range(200):
    new_levels = deepcopy(levels)
    new_levels[0] = tick(levels[0], 0)
    for num in range(1, num_levels//2+1):
        new_levels[num] = tick(levels[num], num)
        new_levels[-num] = tick(levels[-num], -num)
    levels = new_levels

# Answer
cnt = 0
for g in levels.values():
    for line in g:
        cnt += line.count('#')
print(cnt)
