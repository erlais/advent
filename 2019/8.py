data = open('input8').read().strip()

# Part 1
H = 6
W = 25
layer_len = H * W

layers = []
for i in range(0, len(data), layer_len):
    layers.append(data[i:i+layer_len])

cz = {l: l.count('0') for l in layers}
lowest = min(cz, key=cz.get)
# print(lowest.count('1') * lowest.count('2'))  # 2460

# Part 2
image = ''
for i in range(layer_len):
    if i % W == 0:
        image += '\n'
    for layer in layers:
        if layer[i] != '2':
            image += layer[i]
            break

print(image.replace('0', ' '))

# 1    111  1111 1  1 1  1
# 1    1  1 1    1 1  1  1
# 1    1  1 111  11   1  1
# 1    111  1    1 1  1  1
# 1    1 1  1    1 1  1  1
# 1111 1  1 1    1  1  11
