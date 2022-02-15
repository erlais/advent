from itertools import combinations

def part1(buf_size):
    buf = data[:buf_size]
    for line in data[buf_size:]:
        valid = []
        for comb in combinations(buf, 2):
            valid.append(sum(comb) == line)
        if not any(valid):
            return line
        buf.pop(0)
        buf.append(line)

def part2(p1_res):
    data_copy = data.copy()
    res = []
    for line in data:
        for item in data_copy:
            res.append(item)
            sub_sum = sum(res)
            if sub_sum > p1_res:
                data_copy.pop(0)
                res = []
                break
            elif sub_sum == p1_res:
                return sum([min(res), max(res)])

with open('inputs/09.in', 'r') as f:
    data = [int(x) for x in f.read().splitlines()]

part1_res = part1(25)
print('Part1:', part1_res)
print('Part2:', part2(part1_res))
