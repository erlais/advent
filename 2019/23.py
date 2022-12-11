import sys
import logging
from copy import copy

from intcode import Program


class Node(Program):
    def __init__(self, data, ID):
        super().__init__(data)
        self.name = str(ID)
        self.ID = ID
        self.in_val = -1
        self.set_ipaddr()

    def set_ipaddr(self):
        self.in_val_list.append(self.ID)


def main(nodes):
    # Try to get one output from each node
    def tick(n):
        for nid, ngen in enumerate(n):
            # print(f'Node {nodes[nid].name}:')
            # print(f'in_val_list {nodes[nid].in_val_list}')
            target = next(ngen)
            if target == 'idle':
                continue
            x = next(ngen)
            y = next(ngen)
            gather_instr[nid].extend([target, x, y])

    node_gens = [n.runner(do_wait=True) for n in nodes]
    gather_instr = [[] for _ in range(len(nodes))]
    NAT = []
    prev_sent = None

    first_idle = True
    while True:
        tick(node_gens)

        # All nodes are idle, send NAT to node 0
        if not any(gather_instr) and NAT:
            if NAT[1] == prev_sent:
                if not first_idle:
                    print(f'Double Y: {prev_sent}')
                    sys.exit(0)
                first_idle = False
            nodes[0].in_val_list.extend(NAT)
            # print(f'sent {NAT} to node 0')
            prev_sent = NAT[1]
            continue

        # Some node has activity, execute the instructions
        for i, instr in enumerate(gather_instr):
            if len(instr) == 3:  # we have full instruction
                target = instr[0]
                if target == 255:  # save packet in NAT
                    NAT = instr[1:]
                    gather_instr[i] = []
                else:
                    nodes[target].in_val_list.extend(instr[1:])
                    gather_instr[i] = []


if __name__ == "__main__":
    ll = logging.ERROR
    logging.basicConfig(format='%(message)s', level=ll)

    # INIT
    data = open('input23').read().strip().split(',')
    data = [int(x) for x in data]
    extra_mem = [0 for _ in range(10000)]
    data = data + extra_mem

    # Computers
    computers = [Node(copy(data), ID) for ID in range(50)]

    # RUN
    main(computers)
