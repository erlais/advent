from string import ascii_uppercase
from collections import namedtuple, deque, defaultdict
from copy import copy

def get_adjacent(y, x):
    return [(y-1, x), (y+1, x), (y, x-1), (y, x+1)]

def is_portal(grid, y, x):
    res = False
    for k, v in portals.items():
        if (y, x) in v:
            res = True
    return res

def get_port_exit(name, entry):
    coords = portals[name]
    if not len(coords) == 2:
        return None
    return list(coords - {entry})[0]

def inner_outer(grid, y, x):
    """ return 1 if coords are inside donut, -1 if outside (maze level) """
    if 3 < y < len(grid)-3 and 3 < x < len(grid[0])-3:
        return 1
    return -1

def is_path(grid, y, x):
    return grid[y][x] == '.'

def parse_portal(grid, y, x):
    adjacent = get_adjacent(y, x)
    dot_loc = False
    upper_loc = False
    for adj_y, adj_x in adjacent:
        if adj_y in range(0, len(grid)) and adj_x in range(0, len(grid[0])):
            if grid[adj_y][adj_x] == '.':
                dot_loc = (adj_y, adj_x)
                dir_y = y - adj_y
                dir_x = x - adj_x
                # Portal letter ordering is important with real input
                # TODO: find a less verbose way to deal with directions
                if dir_y < 0:
                    upper_letter = grid[y+dir_y][x]
                    portal_name = upper_letter + grid[y][x]
                elif dir_y > 0:
                    upper_letter = grid[y+dir_y][x]
                    portal_name = grid[y][x] + upper_letter
                elif dir_x < 0:
                    upper_letter = grid[y][x+dir_x]
                    portal_name = upper_letter + grid[y][x]
                elif dir_x > 0:
                    upper_letter = grid[y][x+dir_x]
                    portal_name = grid[y][x] + upper_letter
            elif grid[adj_y][adj_x] in ascii_uppercase:
                upper_letter = grid[adj_y][adj_x]
                upper_loc = (adj_y, adj_x)
    if dot_loc and portal_name:
        return portal_name, dot_loc
    return None


lines = open('input20').read().splitlines()
grid = [[char for char in l] for l in lines]

# Create map of portal names and coordinates
portals = defaultdict(set)
for y, row in enumerate(grid):
    for x, col in enumerate(row):
        loc = grid[y][x]
        if loc in ascii_uppercase:
            pp = parse_portal(grid, y, x)
            if pp:
                pname, ploc = pp
                portals[pname].add(ploc)

# Set up state
start_pos = next(iter(portals['AA']))
Status = namedtuple('Status', ('y', 'x', 'lvl', 'dist'))
Q = deque([Status(start_pos[0], start_pos[1], 0, 0)])
seen = set()

while Q:
    teleported = False
    pos = Q.popleft()
    if (pos.y, pos.x) in portals['ZZ'] and pos.lvl == 0:
        print(f'Got to exit in {pos.dist} moves!')
        Q.clear()
        continue
    if pos[:3] in seen:  # don't include distance state in seen
        continue
    seen.add(pos[:3])
    # we on a portal tile (next to portal letter)
    if is_portal(grid, pos.y, pos.x):
        for k, v in portals.items():
            if len(v) > 1 and (pos.y, pos.x) in v:
                dest_y, dest_x = get_port_exit(k, (pos.y, pos.x))
                lvl_change = inner_outer(grid, pos.y, pos.x)
                dest_lvl = pos.lvl + lvl_change
                if dest_lvl >= 0:
                    # print(f'went to level {dest_lvl} @ {k} ({pos.lvl} + {lvl_change}) [{pos.y}, {pos.x}] dist: {pos.dist}')
                    Q.append(Status(dest_y, dest_x, dest_lvl, pos.dist + 1))
    # not at a portal tile
    adj = get_adjacent(pos.y, pos.x)
    for py, px in adj:
        if is_path(grid, py, px):
            Q.append(Status(py, px, pos.lvl, pos.dist + 1))
