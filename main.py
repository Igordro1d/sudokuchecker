import random
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def checkIndividualRow(row: list):
    filter_row = [num for num in row if num !=0]
    return len(filter_row) == len(set(filter_row))

def checkIndividualCol(board: list):
    answer = []
    for r in range(len(board)):
        block = []
        for c in range(len(board)):
            block.append(board[c][r])
        answer.append(block)
    return answer

def divideBlock(board: list):
    """
    Divides the 9x9 board into 3x3 boards
    :param board:
    :return:
    """
    answer = []
    for r in range(3):
        for c in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[3*r + i][3*c + j])
            answer.append(block)
    return answer

def validSudokuBoard(board: list):
    if not all(checkIndividualRow(r) for r in board):
        return False
    if not all(checkIndividualRow(r) for r in divideBlock(board)):
        return False
    if not all(checkIndividualRow(r) for r in checkIndividualCol(board)):
        return False
    return True

def findEmptyCells(board: list):
    """
    Finds empty cells (0) in a board and returns the coordinates of it
    :param board:
    :return:
    """
    emptyCellCoordinates = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 0:
                emptyCellCoordinates.append([r, c])
    return emptyCellCoordinates

def sudokusolver(board: list):
    coordinatesOfEmptyCells = findEmptyCells(board)
    if len(coordinatesOfEmptyCells) == 0:
        return board
    cell = coordinatesOfEmptyCells[0]
    r = cell[0]
    c = cell[1]
    for num in range(1,10):
        board[r][c] = num
        if validSudokuBoard(board):
            result = sudokusolver(board)
            if result is not None:
                return result
        board[r][c] = 0

def createNewBoard():
    """
    adds 0's to each square in the board
    :return:
    """
    board = []
    for i in range(9):
        block = []
        for j in range(9):
            block.append(0)
        board.append(block)
    return board

def generateNewBoard(board: list):
    """
    creates a new board for a new game of sudoku
    :param board:
    :return:
    """
    coordinatesOfEmptyCells = findEmptyCells(board)
    if len(coordinatesOfEmptyCells) == 0:
        return board
    cell = coordinatesOfEmptyCells[0]
    r = cell[0]
    c = cell[1]
    num = list(range(1,10))
    random.shuffle(num)
    for i in num:
        board[r][c] = i
        if validSudokuBoard(board):
            result = generateNewBoard(board)
            if result is not None:
                return result
        board[r][c] = 0

def generateNewPuzzle(board: list, difficulty):
    """
    creates the final board the user will see
    :param board: new generated board
    :param difficulty: difficulty the user wants to play at, removes more spaces depending on difficulty
    :return:
    """
    difficultyDic = {
        'easy': 20,
        'medium': 35,
        'hard': 40
    }
    for i in range(difficultyDic[difficulty.lower()]):
        r = random.randint(0,8)
        c = random.randint(0,8)
        board[r][c] = 0
    return board

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/solve', methods=['POST'])
def solve():
    data = request.get_json()
    board = data['board']
    solved = sudokusolver(board)
    return jsonify({'solved': solved})

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    difficulty = data.get('difficulty', 'medium')
    board = createNewBoard()
    filled = generateNewBoard(board)
    puzzle = generateNewPuzzle(filled, difficulty)
    return jsonify({'board': puzzle})

if __name__ == '__main__':
    app.run(debug=True)


