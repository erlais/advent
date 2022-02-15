from functools import reduce

# Part 1
class Planet:
    def __init__(self, x, y, z):
        self.pos = (x, y, z)
        self.vel = [0, 0, 0]

    def calc_vel(self, other):
        for i in range(3):
            if self.pos[i] < other.pos[i]:
                self.vel[i] += 1
            elif self.pos[i] > other.pos[i]:
                self.vel[i] -= 1

    def update_pos(self):
        self.pos = (self.pos[0] + self.vel[0], self.pos[1] + self.vel[1], self.pos[2] + self.vel[2])

    def calc_nrg(self):
        pot = sum(abs(x) for x in self.pos)
        kin = sum(abs(x) for x in self.vel)
        return pot * kin

planets = [
    Planet(3, 3, 0),
    Planet(4, -16, 2),
    Planet(-10, -6, 5),
    Planet(-3, 0, -13)
]

for _ in range(1000):
    for p in planets:
        for p2 in planets:
            if p.pos == p2.pos:  # skip itself
                continue
            p.calc_vel(p2)

    for p in planets:
        p.update_pos()

res = sum(p.calc_nrg() for p in planets)
print('Part 1:')
print(res)


# Part 2: find alignments of each dimension and their lowest common multiple
class P:
    def __init__(self, x):
        self.pos = x
        self.vel = 0

    def calc_vel(self, other):
        if self.pos < other.pos:
            self.vel += 1
        elif self.pos > other.pos:
            self.vel -= 1

    def update_pos(self):
        self.pos += self.vel

px = [P(3), P(4), P(-10), P(-3)]
py = [P(3), P(-16), P(-6), P(0)]
pz = [P(0), P(2), P(5), P(-13)]

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

def one_dim(planets):
    start_all = tuple(p.pos for p in planets)
    n = 1
    while True:
        # check if we are in start position
        if n > 1 and tuple(p.pos for p in planets) == start_all:
            return n
        # calculate velocity for all planets
        for p in planets:
            for p2 in planets:
                # skip itself
                if p.pos == p2.pos:
                    continue
                p.calc_vel(p2)
        # update position of oll planets
        for p in planets:
            p.update_pos()
        n += 1

print('Part 2:')
print(lcmm(one_dim(px), one_dim(py), one_dim(pz)))
