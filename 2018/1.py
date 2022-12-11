data = open('input1').readlines()
data = [int(x) for x in data]

# Part 1
print(sum(data))

# Part 2
cur_f = 0
seen = set()
i = 0
while True:
    cur_f += data[i]
    if cur_f in seen:
        print(cur_f)
        break
    seen.add(cur_f)
    i += 1
    if i == len(data):
        i = 0
