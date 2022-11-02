with open('inputs/6.in') as f:
    data = [int(x) for x in f.read().split(',')]

fish = {i: 0 for i in range(9)}
for x in data:
    fish[x] += 1

for _ in range(256):
    new_fish = fish.copy()
    for k, v in fish.items():
        if k == 0:
            new_fish[0] = 0
            new_fish[6] += v
            new_fish[8] += v
        else:
            new_fish[k - 1] += v
            new_fish[k] -= v
    fish = new_fish

print(sum(fish.values()))