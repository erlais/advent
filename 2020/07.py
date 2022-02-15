import re

with open('inputs/07.in', 'r') as f:
    data = f.read().splitlines()

def part1(color):
    if color == 'shiny gold':
        return True
    res = []
    for new_color in graph.get(color):
        res.append(part1(new_color[1]))
    return any(res)

def part2(color):
    total = 0
    for num, color in graph[color]:
        total += num + num * part2(color)
    return total

graph = {}
for line in data:
    key = re.match(r'\w+ \w+', line)[0]
    values = re.findall(r'(\d+) (\w+ \w+)', line)
    graph[key] = [(int(k), v) for k, v in values]

part1 = sum(part1(color) for color in graph.keys()) - 1
print('Part1:', part1)
print('Part2:', part2('shiny gold'))
