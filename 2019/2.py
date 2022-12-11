import copy

in_data = open('input2').read().split(',')
in_data = [int(x) for x in in_data]

# Part 1
def run(d1, d2):
    data = copy.copy(in_data)
    data[1] = d1
    data[2] = d2
    i = 0
    while True:
        opcode = data[i]
        if opcode == 99:
            break
        in1, in2, out = data[i+1:i+4]
        if opcode == 1:
            data[out] = data[in1] + data[in2]
        elif opcode == 2:
            data[out] = data[in1] * data[in2]
        i += 4
    return data

print(run(12, 2)[0])  # 3790654


# Part 2
for i in range(100):
    for j in range(100):
        if run(i, j)[0] == 19690720:
            print(i, j)  # 6577
