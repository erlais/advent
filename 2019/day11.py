import logging


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


def make_grid(side_len, def_val=0):
    """ makes a square grid[y][x] """
    grid = []
    for row in range(side_len):
        grid.append([])
        for _ in range(side_len):
            grid[row].append(def_val)
    return grid

class PaintRobot:
    def __init__(self, grid):
        self.grid = grid
        self.pos_x = len(grid[0]) // 2
        self.pos_y = len(grid[0]) // 2
        self.dir = 'U'
        self.paint_count = 0

    def set_color(self, color):
        self.grid[self.pos_y][self.pos_x] = color

    def get_color(self):
        val_in_pos = self.grid[self.pos_y][self.pos_x]
        if val_in_pos not in (0, 1):
            self.paint_count += 1
            return 0
        return val_in_pos

    def move_left(self):
        if self.dir == 'U':
            self.pos_x -= 1
            self.dir = 'L'
        elif self.dir == 'L':
            self.pos_y += 1
            self.dir = 'D'
        elif self.dir == 'D':
            self.pos_x += 1
            self.dir = 'R'
        elif self.dir == 'R':
            self.pos_y -= 1
            self.dir = 'U'

    def move_right(self):
        if self.dir == 'U':
            self.pos_x += 1
            self.dir = 'R'
        elif self.dir == 'R':
            self.pos_y += 1
            self.dir = 'D'
        elif self.dir == 'D':
            self.pos_x -= 1
            self.dir = 'L'
        elif self.dir == 'L':
            self.pos_y -= 1
            self.dir = 'U'

    def do_action(self, color, dir_input):
        self.grid[self.pos_y][self.pos_x] = color
        self.move_right() if dir_input else self.move_left()


def grid_to_str(grid):
    res = ''
    for row in grid:
        res += '\n'
        for col in row:
            res += str(col)
    return res.replace('8', ' ').replace('0', ' ').replace('1', '#')

def main(program):
    grid = make_grid(100, 8)  # 8 is black, but not painted
    robot = PaintRobot(grid)
    robot.set_color(1)  # Part 2
    pgen = program.runner()

    while True:
        program.set_input(robot.get_color())
        out_color = next(pgen)
        out_move = next(pgen)
        if out_color is None:
            break
        robot.do_action(out_color, out_move)

    # print(robot.paint_count)
    print(grid_to_str(robot.grid))


if __name__ == "__main__":
    ll = logging.ERROR
    logging.basicConfig(format='%(message)s', level=ll)

    # INIT
    data = open('input11').read().split(',')
    data = [int(x) for x in data]
    extra_mem = [0 for _ in range(10000)]
    data = data + extra_mem
    prog = Program(data, 'DayEleven')

    # RUN
    main(prog)
