from copy import deepcopy

with open('inputs/11.in', 'r') as f:
    G = [list(row) for row in f.read().splitlines()]

DIRS = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if (i, j) != (0, 0)]

def count_occ(grid):
    return sum(1 for row in grid for col in row if col == '#')

# Part 1
grid = deepcopy(G)
while True:
    new_grid = deepcopy(grid)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            adj = []
            for dr, dc in DIRS:
                if 0 <= dr+r < len(grid) and 0 <= dc+c < len(grid[0]):
                    adj.append(grid[r+dr][c+dc])
            if grid[r][c] == 'L' and '#' not in adj:
                new_grid[r][c] = '#'
            elif grid[r][c] == '#' and adj.count('#') >= 4:
                new_grid[r][c] = 'L'
    if grid == new_grid:
        break
    grid = new_grid
print('Part1:', count_occ(grid))

# Part 2
grid = deepcopy(G)
while True:
    new_grid = deepcopy(grid)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            adj = []
            for dr, dc in DIRS:
                i_dr = r+dr
                i_dc = c+dc
                while 0 <= i_dr < len(grid) and 0 <= i_dc < len(grid[0]):
                    if grid[i_dr][i_dc] == '.':
                        i_dr += dr
                        i_dc += dc
                    else:
                        adj.append(grid[i_dr][i_dc])
                        break
            if grid[r][c] == 'L' and '#' not in adj:
                new_grid[r][c] = '#'
            elif grid[r][c] == '#' and adj.count('#') >= 5:
                new_grid[r][c] = 'L'
    if grid == new_grid:
        break
    grid = new_grid
print('Part2:', count_occ(grid))
