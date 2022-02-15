with open('inputs/06.in', 'r') as f:
    data = f.read().splitlines()

part1 = 0
part2 = 0
answers = []
for line in data:
    if line == '':
        part1 += len(set.union(*answers))
        part2 += len(set.intersection(*answers))
        answers = []
    else:
        answers.append(set(line))

print('Part1:', part1)
print('Part2:', part2)
