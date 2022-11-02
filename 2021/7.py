with open('inputs/7.in') as f:
    data = [int(x) for x in f.read().split(',')]

res = []
for pos in range(min(data), max(data) + 1):
    fuel = 0
    for crab in data:
        for i in range(abs(crab - pos)):
            fuel += i + 1
        if res and fuel > min(res):
            break
    res.append(fuel)

print(min(res))