from collections import defaultdict
from string import ascii_letters


with open('inputs/12.in') as f:
    data = [x.strip() for x in f.readlines()]

def get_adj(r, c):
    return [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

def get_height(char):
    if char == 'S':
        return 0
    elif char == 'E':
        return get_height('z')
    return ascii_letters.index(char)

graph = defaultdict(list)
start = False
end = False
for r in range(len(data)):
    for c in range(len(data[0])):
        if data[r][c] == 'S':
            start = (r, c, 'S')
        elif data[r][c] == 'E':
            end = (r, c, 'E')
        for dr, dc in get_adj(r, c):
            try:
                adj = data[dr][dc]
                graph[(r, c, data[r][c])].append((dr, dc, data[dr][dc]))
            except IndexError:
                pass

def part1():
    Q = [(start, [start])]
    visited = set()
    while Q:
        (node, path) = Q.pop(0)
        if node not in visited:
            if node == end:
                return path[1:]
            visited.add(node)
            for neighbor in graph[node]:
                if get_height(neighbor[-1]) - get_height(node[-1]) in range(-10000, 2):
                    Q.append((neighbor, path + [neighbor]))

# copy pasta, but from 'E' to any 'a'
def part2():
    Q = [(end, [end])]
    visited = set()
    while Q:
        (node, path) = Q.pop(0)
        if node not in visited:
            if node[-1] == 'a':
                return path[1:]
            visited.add(node)
            for neighbor in graph[node]:
                if get_height(node[-1]) - get_height(neighbor[-1]) in range(-10000, 2):
                    Q.append((neighbor, path + [neighbor]))

print(len(part1()))
print(len(part2()))
