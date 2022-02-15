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


lines = open('input18').read().splitlines()
grid = [[char for char in l] for l in lines]

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
        print(f'found all keys in {pos.dist} moves!')
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
            if grid[py][px].lower() in pos.collected:
                Q.append(Status(py, px, pos.collected, pos.dist + 1))
