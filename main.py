from networkx.generators import sudoku
import random

# sudoku_board = [
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]
# sudoku_board2 = [
#     [0, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 0, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 0, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 0, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 0, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 0, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 0, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]

def rowchecker(row: list):
    filter_row = [num for num in row if num !=0]
    if len(filter_row) == len(set(filter_row)):
        return True

def colchecker(board: list):
    answer = []
    for r in range(len(board)):
        block = []
        for c in range(len(board)):
            block.append(board[c][r])
        answer.append(block)
    return answer

def divideblocks(board: list):
    answer = []
    for r in range(3):
        for c in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[3*r + i][3*c + j])
            answer.append(block)
    return answer

def sudokucheck(board: list):
    # for r in board:
    #     if 0 in r:
    #         return False
    #checks each item in board to see if true
    if not all(rowchecker(r) for r in board):
        return False
    if not all(rowchecker(r) for r in divideblocks(board)):
        return False
    if not all(rowchecker(r) for r in colchecker(board)):
        return False
    return True

def emptycell(board: list):
    emptycells = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                emptycells.append([r, c])
    return emptycells

def sudokusolver(board: list):
    emptycells = emptycell(board)
    if len(emptycells) == 0:
        return board
    cell = emptycells[0]
    r = cell[0]
    c = cell[1]
    for num in range(1,10):
        board[r][c] = num
        if sudokucheck(board):
            result = sudokusolver(board)
            if result is not None:
                return result
        board[r][c] = 0

def makeemptyboard():
    board = []
    for i in range(9):
        block = []
        for j in range(9):
            block.append(0)
        board.append(block)
    return board

def generateboard(board: list):
    emptycells = emptycell(board)
    if len(emptycells) == 0:
        return board
    cell = emptycells[0]
    r = cell[0]
    c = cell[1]
    num = list(range(1,10))
    random.shuffle(num)
    for i in num:
        board[r][c] = i
        if sudokucheck(board):
            result = generateboard(board)
            if result is not None:
                return result
        board[r][c] = 0

def puzzlegenerator(board: list, difficulty):
    x=0
    if difficulty.lower() == 'easy':
        x = 20
    elif difficulty.lower() == 'medium':
        x = 35
    elif difficulty.lower() == 'hard':
        x = 40
    for i in range(x):
        r = random.randint(0,8)
        c = random.randint(0,8)
        board[r][c] = 0
    return board




# def generateboard():
#     board=[]
#     for i in range(9):
#         block=[]
#         for j in range(9):
#             block.append(0)
#         board.append(block)
#     for i in range(30):
#         r = random.randint(0,8)
#         c = random.randint(0,8)
#         if board[r][c] == 0:
#             board[r][c] = random.randint(1,9)
#             if not sudokucheck(board):
#                 board[r][c] = 0
#     if sudokucheck(board):
#         return board
#     else:
#         return generateboard()

