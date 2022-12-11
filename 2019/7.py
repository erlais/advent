import copy
import itertools

in_data = open('input7').read().split(',')
in_data = [int(x) for x in in_data]

DEBUG = 0
def debug(in_str):
    if DEBUG:
        print(in_str)

# in_data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
# in_data = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]

def parse_op(in_op):
    op_chars = [x for x in str(in_op)]
    while len(op_chars) < 5:
        op_chars.insert(0, '0')
    last = op_chars.pop(-1)
    op_chars[-1] += last
    return [int(x) for x in op_chars]

def m(obj, param, mode):
    return obj[param] if mode == 0 else param

def run(data, i, in_values, name):
    debug(f'STARTING: Amplifier {name} with inputs {in_values} @ pointer position {i}')
    while True:
        m3, m2, m1, opcode = parse_op(data[i])
        if opcode == 99:
            debug(f'{name}: op [99] => FINISHED!')
            yield None
        if opcode == 3:  # store input
            if len(in_values) > 0:
                target = data[i+1]
                data[target] = in_values.pop(0)
                debug(f'{name}: op [3] => wrote {data[target]} to data[{target}]')
            # else:
            #     debug(f'didnt have in_values @ amp:{name}')
            i += 2
        elif opcode == 4:  # send output
            out = m(data, data[i+1], m1)
            debug(f'{name}: op [4] => sending {out} to next amplifier, storing pointer {i}\n')
            i += 2
            yield data, i, out
        elif opcode == 5:
            debug(f'{name}: op [5] => jump if true')
            if m(data, data[i+1], m1):
                i = m(data, data[i+2], m2)
            else:
                i += 3
        elif opcode == 6:
            debug(f'{name}: op [6] => jump if false')
            if not m(data, data[i+1], m1):
                i = m(data, data[i+2], m2)
            else:
                i += 3
        elif opcode in (1, 2, 7, 8):  # 3 params
            par1, par2, par3 = data[i+1:i+4]
            target = i+3 if m3 else par3
            if opcode == 1:
                x1 = m(data, par1, m1)
                x2 = m(data, par2, m2)
                data[target] = x1 + x2
                debug(f'{name}: op [1] => adding {x1} and {x2} to data[{target}]')
            elif opcode == 2:
                x1 = m(data, par1, m1)
                x2 = m(data, par2, m2)
                data[target] = x1 * x2
                debug(f'{name}: op [2] => multiplying {x1} and {x2} to data[{target}]')
            elif opcode == 7:
                debug(f'{name}: op [7]')
                data[target] = 1 if m(data, par1, m1) < m(data, par2, m2) else 0
            elif opcode == 8:
                debug(f'{name}: op [7]')
                data[target] = 1 if m(data, par1, m1) == m(data, par2, m2) else 0
            i += 4


def loop(phases):
    # init
    amp_names = ('A','B','C','D','E')
    amps = [{'name': amp_names[x], 'data': copy.copy(in_data), 'i': 0, 'inputs': [y]} for x, y in enumerate(phases)]
    amps[0]['inputs'].append(0)  # give initial value of 0 to A

    endit = False
    while not endit:
        for ix, amp in enumerate(amps):
            res = next(run(amp['data'], amp['i'], amp['inputs'], amp['name']))
            if res is None:
                endit = True
                return amp['inputs'][0]

            amps[ix]['data'], amps[ix]['i'], = res[:2]
            if res[2]:
                amps[(ix+1) % len(amps)]['inputs'].append(res[2])


perms = [x for x in itertools.permutations([5,6,7,8,9], 5)]

gg = []
for perm in perms:
    debug(f'trying perm {perm}')
    gg.append(loop(perm))

assert len(perms) == len(gg)
print(max(gg))  # 34579864
