from string import ascii_lowercase, ascii_uppercase
from collections import namedtuple, deque

def get_adjacent(y, x):
    return [(y+y1, x+x1) for y1, x1 in [[-1, 0], [1, 0], [0, -1], [0, 1]]]

def is_tunnel(grid, y, x):
    return grid[y][x] in '.@'

def is_key(grid, y, x):
    return grid[y][x] in ascii_lowercase

def is_door(grid, y, x):
    return grid[y][x] in ascii_uppercase


def run_part(grid):
    keys = {}
    start_pos = None
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            loc = grid[y][x]
            if loc in ascii_lowercase:
                keys[loc] = (y, x)
            elif loc == '@':
                start_pos = (y, x)

    Status = namedtuple('Status', ('y', 'x', 'collected', 'dist'))

    Q = deque([Status(start_pos[0], start_pos[1], tuple(), 0)])
    seen = set()

    while Q:
        pos = Q.popleft()
        if set(pos.collected) == set(keys.keys()):
            return pos.dist
            Q.clear()
            continue
        if pos[:3] in seen:  # don't include distance state in seen
            continue
        seen.add(pos[:3])
        adj = get_adjacent(pos.y, pos.x)
        for py, px in adj:

            if is_tunnel(grid, py, px):
                Q.append(Status(py, px, pos.collected, pos.dist + 1))

            elif is_key(grid, py, px):
                found_key = grid[py][px]
                if found_key in pos.collected:
                    Q.append(Status(py, px, pos.collected, pos.dist + 1))
                    continue
                new_collected = pos.collected + tuple(found_key)
                Q.append(Status(py, px, tuple(sorted(new_collected)), pos.dist + 1))

            elif is_door(grid, py, px):
                # go through door if they key for that door is not in this room
                if grid[py][px].lower() in pos.collected or grid[py][px].lower() not in keys.keys():
                    Q.append(Status(py, px, pos.collected, pos.dist + 1))

lines = open('input18_2').read().splitlines()
grid = [[char for char in l] for l in lines]

half_y = len(lines) // 2 + 1
half_x = len(lines[0]) // 2 + 1
NW = [[c for x, c in enumerate(r) if x < half_x] for y, r in enumerate(grid) if y < half_y]
NE = [[c for x, c in enumerate(r) if x >= half_x - 1] for y, r in enumerate(grid) if y < half_y]
SW = [[c for x, c in enumerate(r) if x < half_x] for y, r in enumerate(grid) if y >= half_y - 1]
SE = [[c for x, c in enumerate(r) if x >= half_x - 1] for y, r in enumerate(grid) if y >= half_y - 1]

res = []
for g in [NW, NE, SW, SE]:
    res.append(run_part(g))
print(sum(res))
