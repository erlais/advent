import logging
from collections import defaultdict
from itertools import cycle

from intcode import Program


def make_grid(side_len, def_val=0):
    """ makes a square grid[y][x] """
    grid = []
    for row in range(side_len):
        grid.append([])
        for _ in range(side_len):
            grid[row].append(def_val)
    return grid

class OxyRobot:
    def __init__(self, grid):
        self.grid = grid
        self.pos_x = len(grid[0]) // 2
        self.pos_y = len(grid[0]) // 2
        self.direction = 4
        self.prev_dir = None
        self.oxy_loc = None

    def move(self, direction):
        x, y = self.get_dir_coords(direction)
        self.pos_y = y
        self.pos_x = x
        self.prev_dir = direction

    def get_dir_coords(self, direction):
        x = self.pos_x
        y = self.pos_y
        if direction == 1:
            y -= 1
        elif direction == 2:
            y += 1
        elif direction == 3:
            x -= 1
        elif direction == 4:
            x += 1
        return x, y

    def get_direction(self):
        """ up (1), down (2), left (3), right (4) """
        clockwise = [4, 2, 3, 1]
        cw = cycle(clockwise)
        while True:
            if not self.prev_dir:
                yield next(cw)
            if self.prev_dir == 1:
                if self.grid[self.pos_y][self.pos_x + 1] == '#':
                    self.prev_dir = 3
                yield 4
            if self.prev_dir == 2:
                if self.grid[self.pos_y][self.pos_x - 1] == '#':
                    self.prev_dir = 4
                yield 3
            if self.prev_dir == 3:
                if self.grid[self.pos_y - 1][self.pos_x] == '#':
                    self.prev_dir = 2
                yield 1
            if self.prev_dir == 4:
                if self.grid[self.pos_y + 1][self.pos_x] == '#':
                    self.prev_dir = 1
                yield 2

    def do_action(self, direction, response):
        if response == 0:
            x, y = self.get_dir_coords(direction)
            self.grid[y][x] = '#'

        elif response == 1:
            self.grid[self.pos_y][self.pos_x] = '.'
            self.move(direction)

        elif response == 2:
            self.grid[self.pos_y][self.pos_x] = '0'
            self.oxy_loc = (self.pos_y, self.pos_x)
            self.move(direction)


def grid_to_str(grid):
    res = ''
    for row in grid:
        res += '\n'
        for col in row:
            res += str(col)
    return res

def grid_to_graph(grid):
    graph = defaultdict(set)
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            if col not in ['.', 'O']:
                continue
            adjacent = [(y+y1, x+x1) for y1, x1 in [[-1, 0], [1, 0], [0, -1], [0, 1]]]
            for adj in adjacent:
                if grid[adj[0]][adj[1]] in ['.', 'O']:
                    graph[(y, x)].add(adj)
    return graph

def find_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def main(program):
    grid = make_grid(50, ' ')
    robot = OxyRobot(grid)
    pgen = program.runner()
    dir_gen = robot.get_direction()
    i = 0
    while i < 5000:
        direction = next(dir_gen)
        program.set_input(direction)
        response = next(pgen)
        robot.do_action(direction, response)
        print(grid_to_str(robot.grid))
        # if robot_status is None:
        #     break
        i += 1

    # Part 1
    mid = len(robot.grid[0]) // 2
    start_loc = (mid, mid)
    oxy_loc = robot.oxy_loc
    graph = grid_to_graph(robot.grid)
    paths = list(find_path(graph, start_loc, oxy_loc))
    print('part1:', len(paths[0]))

    # Part 2 (from oxy to furthest point)
    res = []
    for pos in graph.keys():
        p = list(find_path(graph, oxy_loc, pos))
        if len(p) > 0:
            res.append(len(p[-1]))
    print('part2:', max(res))
        

if __name__ == "__main__":
    ll = logging.ERROR
    logging.basicConfig(format='%(message)s', level=ll)

    # INIT
    data = open('input15').read().split(',')
    data = [int(x) for x in data]
    extra_mem = [0 for _ in range(10000)]
    data = data + extra_mem
    prog = Program(data, 'Day15')

    # RUN
    main(prog)
