import re

with open('inputs/10.in') as f:
    data = [x.strip() for x in f.readlines()]

# Part 1
reduced = []
for row in data:
    before_len = len(row)
    run = True
    while run:
        for chunk in ['()', '[]', '{}', '<>']:
            row = row.replace(chunk, '')
        after_len = len(row)
        if before_len == after_len:
            reduced.append(row)
            run = False
        before_len = after_len

part1 = 0
p1_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
corrupted = []
for i, x in enumerate(reduced):
    if matches := re.findall(r'[\)\]\}\>]', x):
        part1 += p1_scores[matches[0]]
        corrupted.append(i)
print(part1)

# Part 2
res = []
char_map = {'(': ')', '[': ']', '{': '}', '<': '>'}
p2_data = [x for i, x in enumerate(reduced) if i not in corrupted]
for row in p2_data:
    row = list(row)
    completion = []
    while row:
        last_char = row.pop(-1)
        completion.append(char_map[last_char])
    res.append(completion)

p2_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
part2 = []
for row in res:
    row_score = 0
    for x in row:
        row_score *= 5
        row_score += p2_scores[x]
    part2.append(row_score)
print(sorted(part2)[len(part2)//2])
