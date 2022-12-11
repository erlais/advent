import math

with open('inputs/11.in') as f:
    data = [x.strip() for x in f.readlines()]
    data.append('')


class Monkey:
    def __init__(self, items, op, test, t, f):
        self.items = [int(x) for x in items]
        self.op = op
        self.test = int(test)
        self.t = int(t)
        self.f = int(f)
        self.inspected = 0

    def round(self):
        for itm in self.items:
            self.inspected += 1
            amount = self.op[1]
            if self.op[0] == '*':
                if amount == 'old':
                    amount = itm
                itm *= int(amount)
            elif self.op[0] == '+':
                if amount == 'old':
                    amount = itm
                itm += int(amount)
            # itm = itm // 3  # Part 1
            itm = itm % lcm  # Part 2
            if itm % self.test == 0:
                self.throw(self.t, itm)
            else:
                self.throw(self.f, itm)
        self.items = []

    def throw(self, target, itm):
        monkeys[target].items.append(itm)


monkeys = []
args = []
for row in data:
    match row.split():
        case ['Starting', 'items:', *items]:
            items = [x.replace(',', '') for x in items]
            args.append(items)
        case ['Operation:', *op]:
            args.append(op[-2:])
        case ['Test:', *val] | ['If', 'true:', *val] | ['If', 'false:', *val]:
            args.append(val[-1])
        case []:
            monkeys.append(Monkey(*args))
            args = []

lcm = math.prod(x.test for x in monkeys)

for _ in range(10000):
    for monkey in monkeys:
        monkey.round()

res = sorted(x.inspected for x in monkeys)
print(math.prod(res[-2:]))

