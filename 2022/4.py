with open('inputs/4.in') as f:
    data = [x.strip() for x in f.readlines()]

part1 = 0
part2 = 0
for row in data:
    in1, in2, in3, in4 = row.replace(',', '-').split('-')
    r1 = set(range(int(in1), int(in2) + 1))
    r2 = set(range(int(in3), int(in4) + 1))

    bigger_range = max(len(r1), len(r2))
    if len(r1 | r2) == bigger_range:
        part1 += 1

    if len(r1 & r2) > 0:
        part2 += 1

print(part1)
print(part2)
