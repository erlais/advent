import re
from copy import deepcopy

with open('inputs/24.in', 'r') as f:
    inp = f.read().splitlines()

dirs = {
    'se': (-1, 1),
    'sw': (-1, -1),
    'ne': (1, 1),
    'nw': (1, -1),
    'e': (0, 2),
    'w': (0, -2),
}

# Part 1
black = set()
for line in inp:
    directions = re.findall(r'(se|sw|ne|nw|e|w)', line)
    y = x = 0
    for dr in directions:
        y += dirs[dr][0]
        x += dirs[dr][1]
    if (y, x) in black:
        black.remove((y, x))
    else:
        black.add((y, x))
print('Part1:', len(black))


# Part 2
def tile_valid(coords):
    y, x = coords
    if y % 2 == 0 and x % 2 == 0:
        return True
    if y % 2 != 0 and x % 2 != 0:
        return True

white = {(y, x) for x in range(-120, 120) for y in range(-120, 120)}
white = set(filter(tile_valid, white))
white = white - black

tiles = {coord: 0 for coord in white}
tiles.update({coord: 1 for coord in black})

for _ in range(100):
    new_tiles = deepcopy(tiles)
    for (y, x), color in tiles.items():
        adj_black = sum(tiles.get((y+ay, x+ax), 0) for ay, ax in dirs.values())
        if color == 0 and adj_black == 2:
            new_tiles[(y, x)] = 1
        elif color == 1 and (adj_black == 0 or adj_black > 2):
            new_tiles[(y, x)] = 0
    tiles = new_tiles
print('Part2:', sum(tiles.values()))
