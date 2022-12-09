from string import ascii_letters

with open('inputs/3.in') as f:
    data = [x.strip() for x in f.readlines()]

part1 = []
for row in data:
    first = row[len(row)//2:]
    second = row[:len(row)//2]
    inter = set(first) & set(second)
    part1.append(list(inter)[0])

print(sum(ascii_letters.index(x)+1 for x in part1))

part2 = []
for i in range(0, len(data), 3):
    inter = set(data[i]) & set(data[i+1]) & set(data[i+2])
    part2.append(list(inter)[0])

print(sum(ascii_letters.index(x)+1 for x in part2))
