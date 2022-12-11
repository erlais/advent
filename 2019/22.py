class Deck:
    def __init__(self, deck_size):
        self.deck_size = deck_size
        self.cards = self.make_cards()

    def make_cards(self):
        return [x for x in range(self.deck_size)]

    def cut(self, num):
        c = self.cards[:num]
        self.cards = self.cards[num:] + c

    def deal_stack(self):
        self.cards = self.cards[::-1]

    def deal_incr(self, N):
        table = [None for _ in range(self.deck_size)]
        i = 0
        for card in self.cards:
            table[i % self.deck_size] = card
            i += N
        self.cards = table


# Part 1
data = open('input22').read().strip()
instructions = data.splitlines()
d = Deck(10007)

for instr in instructions:
    if 'deal with increment' in instr:
        n = int(instr.split()[-1])
        d.deal_incr(n)
    elif instr == 'deal into new stack':
        d.deal_stack()
    elif instr.startswith('cut'):
        c = int(instr.split()[-1])
        d.cut(c)
print(d.cards.index(2019))

# Part 2
pos = 2020
size = 119315717514047
iterations = 101741582076661

increment_mul = 1
offset_diff = 0

for instr in instructions:
    if 'deal with increment' in instr:
        n = int(instr.split()[-1])
        increment_mul *= pow(n, size - 2, size)
    elif instr == 'deal into new stack':
        increment_mul *= -1
        offset_diff += increment_mul
    elif instr.startswith('cut'):
        n = int(instr.split()[-1])
        offset_diff += n * increment_mul

    increment_mul %= size
    offset_diff %= size

increment = pow(increment_mul, iterations, size)
offset = offset_diff * (1 - increment) * pow((1 - increment_mul) % size, size - 2, size)
offset %= size

pos = (offset + pos * increment) % size 
print(pos)
