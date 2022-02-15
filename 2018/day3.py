data = open('input3').readlines()
claims = []
for line in data:
    c = {}
    line = line.strip()
    parts = line.split()
    c['id'] = parts[0][1:]
    c['pos'] = [int(x) for x in parts[2][:-1].split(',')]
    c['size'] = [int(x) for x in parts[3].split('x')]
    claims.append(c)

# Part 1
grid = [[0 for _ in range(1000)] for _ in range(1000)]
for claim in claims:
    pl, pt = claim['pos']
    size_x, size_y = claim['size']
    for x in range(pl, pl + size_x):
        for y in range(pt, pt + size_y):
            grid[y][x] += 1

res = 0
for row in grid:
    for col in row:
        if col > 1:
            res += 1
print(res)

# Part 2
for claim in claims:
    pl, pt = claim['pos']
    size_x, size_y = claim['size']
    overlaps = False
    for x in range(pl, pl + size_x):
        for y in range(pt, pt + size_y):
            if grid[y][x] > 1:
                overlaps = True
    if not overlaps:
        print(claim['id'])

