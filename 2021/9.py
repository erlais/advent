import math
from collections import defaultdict

with open('inputs/9.in') as f:
    data = [x.strip() for x in f.readlines()]

G = [[[] for _ in range(len(data[0]))] for x in data]
for r, row in enumerate(data):
    for c, col in enumerate(row):
        G[r][c] = int(col)

# Part 1
lowest = []
for r, row in enumerate(G):
    for c, col in enumerate(row):
        is_smallest = True
        for ar, ac in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if ar < 0 or ac < 0 or ar > len(G)-1 or ac > len(G[0])-1:
                continue
            if G[ar][ac] <= G[r][c]:
                is_smallest = False
        if is_smallest:
            lowest.append((r, c))

part1 = sum(G[r][c] + 1 for r, c in lowest)
print(part1)

# Part 2
basins = defaultdict(int)
Q = [(r, c, idx) for idx, (r, c) in enumerate(lowest)]
SEEN = set()
while Q:
    r, c, idx = Q.pop(0)
    for ar, ac in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
        if ar < 0 or ac < 0 or ar > len(G)-1 or ac > len(G[0])-1:
            continue
        if G[ar][ac] == 9:
            continue
        if G[ar][ac] > G[r][c]:
            if (ar, ac, idx) not in SEEN:
                SEEN.add((ar, ac, idx))
                Q.append((ar, ac, idx))
                basins[idx] += 1

top3 = sorted([x + 1 for x in basins.values()], reverse=True)[:3]
print(math.prod(top3))
