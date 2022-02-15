data = open('input5').read().split(',')
data = [int(x) for x in data]

def parse_op(in_op):
    op_chars = [x for x in str(in_op)]
    while len(op_chars) < 5:
        op_chars.insert(0, '0')
    last = op_chars.pop(-1)
    op_chars[-1] += last
    return [int(x) for x in op_chars]

def m(obj, param, mode):
    return obj[param] if mode == 0 else param

in_val = 5
i = 0
while True:
    m3, m2, m1, opcode = parse_op(data[i])
    if opcode == 99:
        break
    if opcode == 3:
        target = data[i+1]
        data[target] = in_val
        i += 2
    elif opcode == 4:
        print(m(data, data[i+1], m1))
        i += 2
    elif opcode == 5:
        if m(data, data[i+1], m1):
            i = m(data, data[i+2], m2)
        else:
            i += 3
    elif opcode == 6:
        if not m(data, data[i+1], m1):
            i = m(data, data[i+2], m2)
        else:
            i += 3
    elif opcode in (1, 2, 7, 8):  # 3 params
        par1, par2, par3 = data[i+1:i+4]
        target = i+3 if m3 else par3
        if opcode == 1:
            data[target] = m(data, par1, m1) + m(data, par2, m2)
        elif opcode == 2:
            data[target] = m(data, par1, m1) * m(data, par2, m2)
        elif opcode == 7:
            data[target] = 1 if m(data, par1, m1) < m(data, par2, m2) else 0
        elif opcode == 8:
            data[target] = 1 if m(data, par1, m1) == m(data, par2, m2) else 0
        i += 4
