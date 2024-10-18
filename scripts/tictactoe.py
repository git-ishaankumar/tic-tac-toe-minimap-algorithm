import numpy as np
import math
import random

def check_winner(brd, player):
    for i in range(3):
        if np.all(brd[i, :] == player) or np.all(brd[:, i] == player):
            return True
    if brd[0, 0] == brd[1, 1] == brd[2, 2] == player:
        return True
    if brd[0, 2] == brd[1, 1] == brd[2, 0] == player:
        return True
    return False

def is_full(brd):
    return not np.any(brd == '*')

def minimax(brd, depth, is_maximizing):
    if check_winner(brd, 'X'):
        return -1
    if check_winner(brd, 'O'):
        return 1
    if is_full(brd):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if brd[i, j] == '*':
                    brd[i, j] = 'O'
                    score = minimax(brd, depth + 1, False)
                    brd[i, j] = '*'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if brd[i, j] == '*':
                    brd[i, j] = 'X'
                    score = minimax(brd, depth + 1, True)
                    brd[i, j] = '*'
                    best_score = min(score, best_score)
        return best_score

def pick_best_move(board):
    possible_moves = []
    for i in range(3):
        for j in range(3):
            if board[i, j] == '*':
                board[i, j] = 'O'
                score = minimax(board, 0, False)
                board[i, j] = '*'
                possible_moves.append((score, (i, j)))

    possible_moves.sort(reverse=True, key=lambda x: x[0])
    best_score = possible_moves[0][0]

    if best_score == 1:
        return possible_moves[0][1]

    if best_score == -1:
        for score, move in possible_moves:
            if score == -1:
                return move

    top_moves = [move for score, move in possible_moves if score == best_score]
    if len(top_moves) > 0:
        return random.choice(top_moves)

    return possible_moves[-1][1]
