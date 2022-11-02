with open('inputs/1.in') as f:
    data = [int(x.strip()) for x in f.readlines()]

res = 0
prev = False
for reading in data:
    if prev and reading > prev:
        res += 1
    prev = reading
print(res)


res = 0
prev = False
for i, reading in enumerate(data):
    if i == len(data) - 2:
        break
    window = reading + data[i+1] + data[i+2]
    if prev and window > prev:
        res += 1
    prev = window
print(res)
