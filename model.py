import pickle
import random

with open('network.pickle', 'rb') as handle:
    model = pickle.load(handle)


def flatten_board(board):
    """ Turns the 3x3 board into a 1x9 board """
    return [cell for row in board for cell in row]


def pre_process(board, turn="x"):
    """ Takes the board with x and o and turns in into vectors with numbers. 1 is AI, -1 is human, and 0 is empty """
    result = []

    opposite = "o" if turn == "x" else "x"
    result = [1 if x == turn else x for x in board]
    result = [-1 if x == opposite else x for x in result]
    return result


def next_play(board):
    board = flatten_board(board)
    next_move = None
    tries = 0

    while next_move == None and tries < 30:

        prediction = model.predict([pre_process(board, "o")])
        print("before: ", board[prediction[0]])
        if board[prediction[0]] == 0:
            next_move = prediction[0]
        tries = tries + 1

    if next_move == None:
        next_move = random.choice([i for i, x in enumerate(board) if x == 0])
    # print("play: ", prediction[0], board[prediction[0]])
    return next_move
