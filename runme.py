import pygame as pg
import numpy as np
from scripts.tictactoe import pick_best_move, check_winner, is_full

pg.init()

screen = pg.display.set_mode((300, 400))
pg.display.set_caption('Tic-Tac-Toe')

board = np.array([['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']])
player_turn = True
game_over = False
message = ''
button_rect = pg.Rect(100, 350, 100, 40)

def draw_board():
    for row in range(1, 3):
        pg.draw.line(screen, (0, 0, 0), (0, row * 100), (300, row * 100), 2)
        pg.draw.line(screen, (0, 0, 0), (row * 100, 0), (row * 100, 300), 2)

def draw_marks():
    for i in range(3):
        for j in range(3):
            if board[i, j] == 'X':
                pg.draw.line(screen, (255, 0, 0), (j * 100 + 20, i * 100 + 20), (j * 100 + 80, i * 100 + 80), 4)
                pg.draw.line(screen, (255, 0, 0), (j * 100 + 80, i * 100 + 20), (j * 100 + 20, i * 100 + 80), 4)
            elif board[i, j] == 'O':
                pg.draw.circle(screen, (0, 0, 255), (j * 100 + 50, i * 100 + 50), 40, 4)

def handle_click(x, y):
    global player_turn
    if board[y, x] == '*' and not game_over:
        board[y, x] = 'X' if player_turn else 'O'
        player_turn = not player_turn

def computer_move():
    global player_turn
    move = pick_best_move(board)
    if move:
        board[move[0], move[1]] = 'O'
    player_turn = True

def check_game_over():
    global game_over, message
    if check_winner(board, 'X'):
        game_over = True
        message = 'You win!'
    if check_winner(board, 'O'):
        game_over = True
        message = 'Computer wins!'
    if is_full(board) and not game_over:
        game_over = True
        message = 'Draw!'

def draw_play_again_button():
    pg.draw.rect(screen, (0, 255, 0), button_rect)
    font = pg.font.Font(None, 36)
    text = font.render('Play Again', True, (0, 0, 0))
    screen.blit(text, (button_rect.x + 10, button_rect.y + 5))

def reset_game():
    global board, player_turn, game_over, message
    board = np.array([['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']])
    player_turn = True
    game_over = False
    message = ''

while True:
    screen.fill((255, 255, 255))
    draw_board()
    draw_marks()
    if game_over:
        font = pg.font.Font(None, 36)
        text = font.render(message, True, (0, 0, 0))
        screen.blit(text, (100, 310))
        draw_play_again_button()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if game_over and button_rect.collidepoint(event.pos):
                reset_game()
            elif player_turn and not game_over:
                x = event.pos[0] // 100
                y = event.pos[1] // 100
                handle_click(x, y)
                check_game_over()

    if not player_turn and not game_over:
        computer_move()
        check_game_over()

    pg.display.update()
