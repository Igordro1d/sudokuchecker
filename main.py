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

def rowchecker(row: list):
    if len(row) == len(set(row)):
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
    #checks each item in board to see if true
    if not all(rowchecker(r) for r in board):
        return False
    if not all(rowchecker(r) for r in divideblocks(board)):
        return False
    if not all(rowchecker(r) for r in colchecker(board)):
        return False
    return True


##print(sudokucheck(sudoku_board))