import logging
from collections import deque

class Program:
    def __init__(self, data, name='Program'):
        self.data = data
        self.name = name
        self.ip = 0
        self.rel_base = 0
        self.in_val = 0
        self.in_val_list = deque()

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

    def runner(self, do_wait=False):
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
                in_val = self.in_val_list.popleft() if self.in_val_list else self.in_val
                logging.info('%s @ %s: op [3] => INPUT', self.name, self.ip)
                p1 = self.get_pars(1)
                self.data[self.mode_out(p1)] = in_val
                if do_wait and (not self.in_val_list):
                    yield 'idle'
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

