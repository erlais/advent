from collections import defaultdict

with open('inputs/5.in') as f:
    data = [x.strip() for x in f.readlines()]
    data = [x.replace(' -> ', ',') for x in data]


G = defaultdict(int)
for row in data:
    x1, y1, x2, y2 = [int(x) for x in row.split(',')]
    if x1 == x2:
        len_y = abs(y2 - y1) + 1
        new_y = y2 if y1 > y2 else y1
        for i in range(len_y):
            G[(x1, new_y + i)] += 1
    elif y1 == y2:
        len_x = abs(x2 - x1) + 1
        new_x = x2 if x1 > x2 else x1
        for i in range(len_x):
            G[(new_x + i, y1)] += 1
    else:  # diagonal
        lx = x2 - x1
        ly = y2 - y1
        assert abs(lx) == abs(ly)  # check 45deg
        dirx = 1 if x1 < x2 else -1
        diry = 1 if y1 < y2 else -1
        diag_x = range(x1, x2 + dirx, dirx)
        diag_y = range(y1, y2 + diry, diry)
        for coord in zip(diag_x, diag_y):
            G[coord] += 1

res = 0
for v in G.values():
    if v > 1:
        res += 1
print(res)
