# Завдання 6
# Написати гру "Хрестики-нулики".
#
# Гра включає два режими:
#
# Людина — Людина
# Людина — Комп'ютер.
# Загальна функціональність:
#
# Поле: 3x3, клітини позначені номерами 1-9.
# Правила:
# Гравці по черзі ставлять "X" або "O".
# Перемагає гравець, який склав лінію з трьох символів.
# Якщо поле заповнене, а лінії немає, оголошується нічия.
# Режими:
#
# Людина — Людина:
# Два гравці вводять свої ходи по черзі.
# Перевірка коректності введення і стану гри (перемога, нічия).
# Людина — Комп'ютер:
# Гравець вводить хід, комп'ютер вибирає клітину:
# Простий рівень: випадковий вибір.
# Середній рівень: блокування виграшу гравця.
# Складний рівень: оптимальний хід, спрямований на перемогу комп'ютера.
# Під час завершення гри програма пропонує почати гру заново.
from random import randint

WIN_LINES = [
(0, 1, 2), (3, 4, 5), (6, 7, 8),
(0, 3, 6), (1, 4, 7), (2, 5, 8),
(0, 4, 8), (2, 4, 6)
    ]

def create_board():
    return ["1","2","3","4","5","6","7","8","9"]

def print_board(board):
    for i in range(0,9,3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("--+---+--")

def get_human_move(board, symbol):
    print("Enter number of section where you want to make a move.")
    print(f"You are {symbol}")
    move = input()
    try:
        move = int(move)
    except ValueError:
        print("Please enter a number.")
        return get_human_move(board, symbol)
    if move not in range(1,10):
        print("Move is out of range. Please use 1-9.")
        return get_human_move(board, symbol)
    if board[move - 1] in ["X", "O"]:  #if board[move -1] == "X" or board[move -1] == "O":
        print("That field is already occupied. Please try again.")
        return get_human_move(board, symbol)
    return move

def make_move(board, move, symbol):
    board[move - 1] = symbol

def check_winner(board):
    for a,b,c in WIN_LINES:
        if board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_draw(board):
    for cell in board:
        if cell not in ["X", "O"]:
            return False
    return True

def switch_player(symbol):
    if symbol == "X":
        return "O"
    else:
        return "X"

def available_moves(board):
    available_moves = []
    for i in range(9):
        if board[i] not in ["X", "O"]:
            available_moves.append(i + 1)
    return available_moves

def play_human_vs_human():
    board = create_board()
    symbol = "X"
    while True:
        print_board(board)
        move = get_human_move(board, symbol)
        make_move(board, move, symbol)
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"The winner is {winner}.")
            break
        if is_draw(board):
            print_board(board)
            print(f"Draw.")
            break
        symbol = switch_player(symbol)

#>>>>>>>>>>>>>>>>>>>>>Human VS Computer<<<<<<<<<<<<<<<<<<
import random

def computer_easy(board):
    while True:
        move = random.randint(1,9)
        if board[move - 1] not in ["X", "O"]:
            return move

def computer_medium(board):
    for move in available_moves(board):
        make_move(board, move, "O")
        if check_winner(board) == "O":
            board[move - 1] = str(move)
            return move
        board[move -1] = str(move)
    for move in available_moves(board):
        make_move(board, move, "X")
        if check_winner(board) == "X":
            board[move - 1] = str(move)
            return move
        board[move - 1] = str(move)
    return computer_easy(board)

def minimax(board,depth, is_maximizing):
    winner = check_winner(board)
    if winner == "O":
        return 10 - depth
    if winner == "X":
        return depth - 10
    if is_draw(board):
        return 0

    if is_maximizing:
        best_score = -1000
        for move in available_moves(board):
            make_move(board, move, "O")
            score  = minimax(board, depth + 1, False)
            board[move - 1 ] = str(move)
            if score > best_score: best_score = score
        return best_score
    else:
        best_score = 1000
        for move in available_moves(board):
            make_move(board, move, "X")
            score = minimax(board, depth + 1, True)
            board[move - 1 ] = str(move)
            if score < best_score: best_score = score
        return best_score

def computer_hard(board):
    best_score = -1000
    move = None






