with open('inputs/4.in') as f:
    data = [x.strip() for x in f.readlines()]
    data = [x for x in data if x != '']
    pool = data.pop(0).split(',')
    boards = []
    board = []
    for i, line in enumerate(data):
        numbers = [[x, 0] for x in line.split()]
        board.append(numbers)
        i += 1
        if i % 5 == 0:
            boards.append(board)
            board = []

def win_condition(row_or_col):
    return all(x[1] for x in row_or_col)

def get_winning_boards(boards):
    res = []
    for ix, board in enumerate(boards):
        for y in range(5):
            col = []
            for x in range(5):
                col.append(board[x][y])
            if win_condition(board[y]) or win_condition(col):
                res.append(board)
    return res

def sum_unmarked(board):
    res = 0
    for y in range(5):
        for x in range(5):
            if board[y][x][1] == 0:
                res += int(board[y][x][0])
    return res

WON = []
for draw in pool:
    for board in boards:
        for y in range(5):
            for x in range(5):
                if board[y][x][0] == draw:
                    board[y][x][1] = 1
    if win_boards := get_winning_boards(boards):
        for wb in win_boards:
            WON.append([wb, int(draw)])
            try:
                boards.remove(wb)
            except ValueError:  # same board won on row and col at the same time
                continue

print('Part 1: ', sum_unmarked(WON[0][0]) * WON[0][1])
print('Part 2: ', sum_unmarked(WON[-1][0]) * WON[-1][1])