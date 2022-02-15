from math import prod

with open('inputs/03.in', 'r') as f:
    rows = f.read().splitlines()

def count_trees(slope_x, slope_y):
    res = x = y = 0
    while y < len(rows)-1:
        x += slope_x
        y += slope_y
        if rows[y][x % len(rows[0])] == '#':
            res += 1
    return res

print('Part1:', count_trees(3, 1))
print('Part2:', prod([
    count_trees(1, 1),
    count_trees(3, 1),
    count_trees(5, 1),
    count_trees(7, 1),
    count_trees(1, 2),
]))
