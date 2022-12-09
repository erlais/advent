from collections import defaultdict
from math import prod

with open('inputs/8.in') as f:
    data = [row.strip() for row in f.readlines()]

col_len = len(data)
row_len = len(data[0])

G = [[c for c in r] for r in data]
visible = []
views = defaultdict(list)
res = []

# row left to right
for r in range(row_len):
    seen = []
    for c in range(col_len):
        tree = int(G[r][c])
        highest_seen = max(seen) if seen else -1
        if tree > highest_seen:
            res.append((r,c,tree))
        views[(r, c)].append(seen.copy())
        seen.append(tree)

# row right to left
for r in range(row_len):
    seen = []
    for c in range(col_len-1, -1, -1):
        tree = int(G[r][c])
        highest_seen = max(seen) if seen else -1
        if tree > highest_seen:
            res.append((r,c,tree))
        views[(r, c)].append(seen.copy())
        seen.append(tree)

# col top to bottom
for r in range(row_len):
    seen = []
    for c in range(col_len):
        tree = int(G[c][r])
        highest_seen = max(seen) if seen else -1
        if tree > highest_seen:
            res.append((c,r,tree))
        views[(c, r)].append(seen.copy())
        seen.append(tree)

# col bottom to top
for r in range(row_len):
    seen = []
    for c in range(col_len-1, -1, -1):
        tree = int(G[c][r])
        highest_seen = max(seen) if seen else -1
        if tree > highest_seen:
            res.append((c,r,tree))
        views[(c, r)].append(seen.copy())
        seen.append(tree)


print(len(set(res)))

scores = []
for r, c, _ in res:
    current = int(G[r][c])
    tmp = []
    for path in views[(r, c)]:
        scr = 0
        for t in path[::-1]:
            scr += 1
            if t >= current:
                break
        tmp.append(scr)
    scores.append(tmp)

print(max(prod(x) for x in scores))
