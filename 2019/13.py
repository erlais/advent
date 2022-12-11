import logging
import time
import copy


class Program:
    def __init__(self, data, name='Program'):
        self.data = data
        self.name = name
        self.ip = 0
        self.rel_base = 0
        self.in_val = 0

    def parse_op(self):
        chars = list(str(self.data[self.ip]).zfill(5))
        self.par_modes = [int(chars.pop(-3)) for _ in range(3)]
        self.opcode = int(''.join(chars))
        logging.debug('Function parse_op() => opcode: %s, par_modes: %s', self.opcode, self.par_modes)

    def get_pars(self, num_pars):
        """ pm_dict {parameter: param_mode} """
        res = []
        for i in range(num_pars):
            pm_dict = {
                'p': self.data[self.ip + 1 + i],
                'm': self.par_modes[i]
            }
            res.append(pm_dict)
        logging.debug('Function get_pars() => res: %s', res)
        return res if num_pars > 1 else res[0]

    def mode_in(self, par):
        """ par: dict from self.get_pars """
        logging.debug('Function mode_in(%s) called', par)
        if par['m'] == 0:
            return self.data[par['p']]
        if par['m'] == 1:
            return par['p']
        if par['m'] == 2:
            return self.data[self.rel_base + par['p']]
        raise Exception('Invalid input mode!')

    def mode_out(self, par):
        """ par: dict from self.get_pars """
        logging.debug('Function mode_out(%s) called', par)
        # if ever need mode 1, add offset arg and return self.ip + offset
        assert par['m'] != 1  # can't write to type <int>
        if par['m'] == 0:
            return par['p']
        if par['m'] == 2:
            return self.rel_base + par['p']
        raise Exception('Invalid output mode!')

    def set_input(self, in_val):
        logging.warning('Input Value changed %s => %s', self.in_val, in_val)
        self.in_val = in_val

    def runner(self):
        while True:
            self.parse_op()

            if self.opcode == 99:
                logging.info('%s @ %s: op [99] => FINISHED', self.name, self.ip)
                yield None

            elif self.opcode == 1:
                logging.info('%s @ %s: op [1] => ADD', self.name, self.ip)
                p1, p2, p3 = self.get_pars(3)
                self.data[self.mode_out(p3)] = self.mode_in(p1) + self.mode_in(p2)
                self.ip += 4

            elif self.opcode == 2:
                logging.info('%s @ %s: op [2] => MULTIPLY', self.name, self.ip)
                p1, p2, p3 = self.get_pars(3)
                self.data[self.mode_out(p3)] = self.mode_in(p1) * self.mode_in(p2)
                self.ip += 4

            elif self.opcode == 3:
                logging.info('%s @ %s: op [3] => WRITE', self.name, self.ip)
                p1 = self.get_pars(1)
                self.data[self.mode_out(p1)] = self.in_val
                self.ip += 2

            elif self.opcode == 4:
                logging.info('%s @ %s: op [4] => OUTPUT', self.name, self.ip)
                p1 = self.get_pars(1)
                yield self.mode_in(p1)
                self.ip += 2

            elif self.opcode == 5:
                logging.info('%s @ %s: op [5] => JUMP-IF-TRUE', self.name, self.ip)
                p1, p2 = self.get_pars(2)
                self.ip = self.mode_in(p2) if self.mode_in(p1) else self.ip + 3

            elif self.opcode == 6:
                logging.info('%s @ %s: op [6] => JUMP-IF-FALSE', self.name, self.ip)
                p1, p2 = self.get_pars(2)
                self.ip = self.mode_in(p2) if not self.mode_in(p1) else self.ip + 3

            elif self.opcode == 7:
                logging.info('%s @ %s: op [7] => LESS-THAN', self.name, self.ip)
                p1, p2, p3 = self.get_pars(3)
                target = self.mode_out(p3)
                self.data[target] = 1 if self.mode_in(p1) < self.mode_in(p2) else 0
                self.ip += 4

            elif self.opcode == 8:
                logging.info('%s @ %s: op [8] => EQUALS', self.name, self.ip)
                p1, p2, p3 = self.get_pars(3)
                target = self.mode_out(p3)
                self.data[target] = 1 if self.mode_in(p1) == self.mode_in(p2) else 0
                self.ip += 4

            elif self.opcode == 9:
                logging.info('%s @ %s: op [9] => RELATIVE-BASE', self.name, self.ip)
                p1 = self.get_pars(1)
                self.rel_base += self.mode_in(p1)
                self.ip += 2


def make_grid(x, y, def_val=0):
    """ makes a grid[y][x] """
    return [[def_val for _ in range(x)] for _ in range(y)]

class Arcade:
    def __init__(self, grid):
        self.grid = grid
        self.pos_x = 0
        self.pos_y = 0
        self.score = 0
        self.tiles = {0: ' ', 1: '#', 2: '*', 3: '_', 4: 'O'}
        self.ball_x = False
        self.pad_x = False

    def set_tile(self, instr):
        x, y, tile_id = instr
        if x == -1 and y == 0:
            self.score = tile_id
        else:
            self.grid[y][x] = self.tiles[tile_id]
            if tile_id == 3:
                self.pad_x = x
            if tile_id == 4:
                self.ball_x = x

    def render(self):
        for row in self.grid:
            print(''.join(row))
        print('#' * len(self.grid[1]))

    def count_blocks(self):
        cnt = 0
        for row in self.grid:
            cnt += row.count('*')
        return cnt



def main(program, do_render=False):
    w, h = (44, 24)
    grid = make_grid(w, h, ' ')
    arc = Arcade(grid)
    pgen = program.runner()

    i = 0
    while True:
        instr = (next(pgen), next(pgen), next(pgen))
        if None in instr:
            break
        arc.set_tile(instr)
        i += 1
        # first render after grid is populated.
        # then render every second instruction because it takes 2 moves to change ball position
        if i > w*h and i % 2:
            if arc.ball_x > arc.pad_x:
                new_input = 1
            elif arc.ball_x == arc.pad_x:
                new_input = 0
            else:
                new_input = -1
            if do_render:
                arc.render()
                print(arc.score)
            program.set_input(new_input)
    if not do_render:
        print(f'Final score: {arc.score}')


if __name__ == "__main__":
    ll = logging.ERROR
    logging.basicConfig(format='%(message)s', level=ll)

    # INIT
    data = open('input13').read().split(',')
    data = [int(x) for x in data]
    extra_mem = [0 for _ in range(1000000)]
    data = data + extra_mem
    data[0] = 2
    prog = Program(data, 'Day13')

    # RUN
    main(prog)
