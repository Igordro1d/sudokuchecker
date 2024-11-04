from flask import Flask, jsonify, request
from main import rowchecker, colchecker, divideblocks, sudokucheck, emptycell, sudokusolver, makeemptyboard, generateboard, puzzlegenerator
import random

app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def generate_puzzle():
    data = request.json
    difficulty = data.get('difficulty', 'easy')
    board = makeemptyboard()
    generateboard(board)
    puzzle = puzzlegenerator(board, difficulty)
    return jsonify(puzzle=puzzle)

@app.route('/check', methods=['POST'])
def check_solution():
    data = request.json
    board = data.get("board")
    is_valid = sudokucheck(board)
    return jsonify(valid=is_valid)

if __name__ == '__main__':
    app.run(debug=True)