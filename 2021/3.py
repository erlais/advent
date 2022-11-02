with open('inputs/3.in') as f:
    data = [x.strip() for x in f.readlines()]

NUMLEN = len(data[0])

# Part 1
gamma = ''
for i in range(0, NUMLEN):
    col = [x[i] for x in data]
    gamma += max(set(col), key=col.count)
gamma = int(gamma, 2)
epsilon = ~gamma & 0xfff

print(gamma * epsilon)

# Part 2
def part2(data, pos, high=True):
    col = [x[pos] for x in data]
    count_0 = col.count('0')
    count_1 = col.count('1')
    if high:
        mask = '1' if count_1 >= count_0 else '0'
    else:
        mask = '1' if count_0 > count_1 else '0'
    return [x for x in data if x[pos] == mask]

oxy_list = co2_list = data
for i in range(0, NUMLEN):
    if len(oxy_list) > 1:
        oxy_list = part2(oxy_list, i)
    if len(co2_list) > 1:
        co2_list = part2(co2_list, i, False)

oxy = int(oxy_list[0], 2)
co2 = int(co2_list[0], 2)
print(oxy * co2)
