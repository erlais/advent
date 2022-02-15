import math
from collections import OrderedDict

data = open('input10').readlines()

# Part 1
def magnitude(vector):
    return math.sqrt(vector[0]**2 + vector[1]**2)

asters = []
for y, line in enumerate(data):
    for x, char in enumerate(line):
        if char == '#':
            asters.append((x, y))

res = {}
for x, y in asters:
    norms = set()
    for x2, y2 in asters:
        rel_x = x2 - x
        rel_y = y2 - y
        magn = magnitude((rel_x, rel_y))
        if magn:
            norms.add((round(rel_x/magn, 5), round(rel_y/magn, 5)))
    res[(x, y)] = norms

best = max(res, key=lambda x: len(res[x]))
print(f'best asteroid at {best} that sees {len(res[best])} asteroids')

# Part 2
def get_angle(vector):
    return math.degrees(math.atan2(vector[1], vector[0]))

bx, by = best
all_dict = {(x, y): get_angle((bx-x, by-y)) for x, y in asters}

sorted_all = OrderedDict(sorted(all_dict.items(), key=lambda x: x[1]))

search_angles = list(sorted({x for x in sorted_all.values() if x >= 90.0}))
search_angles += list(sorted({x for x in sorted_all.values() if x < 90.0}))

n = 1
while len(sorted_all) > 0:
    for sa in search_angles:
        matched = [point for point, angle in sorted_all.items() if angle == sa]
        if matched:
            closest = min((bx-x + by-y, (x, y)) for x, y in matched)  # (distance, (point))
            del sorted_all[closest[1]]
            print(f'{n}: nuked {closest[1]}')
            n += 1
