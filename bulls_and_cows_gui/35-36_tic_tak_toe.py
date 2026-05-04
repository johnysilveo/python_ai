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

def ask_restart():
    answer = input("Do you want to restart? (y/n) or menu").strip().lower()
    if answer == "y" or answer == "yes":
        return True
    if answer == "n" or answer == "no":
        return False
    print("Please restart the computer.")
    if answer == "menu" or answer == "m":
        return main_menu()
    return ask_restart()

#>>>>>>>>>>>>>>>>>>>>>Human VS Human<<<<<<<<<<<<<<<<<<

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

#>>>>>>>>>>>>>>>>>>>>>Computer<<<<<<<<<<<<<<<<<<

def computer_easy(board):
    while True:
        move = randint(1,9)
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
    best_move = None
    for move in available_moves(board):
        make_move(board, move, "O")
        score = minimax(board, 0, False)
        board[move - 1 ] = str(move)
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

#>>>>>>>>>>>>>>>>>>>>>>>>End Computer<<<<<<<<<<<<<<<<<<<<<

#>>>>>>>>>>>>>>>>>>>>>Human VS Computer<<<<<<<<<<<<<<<<<<

def play_human_vs_computer(difficulty):
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
        if difficulty == "easy":
            computer_move = computer_easy(board)
        elif difficulty == "medium":
            computer_move = computer_medium(board)
        elif difficulty == "hard":
            computer_move = computer_hard(board)
        make_move(board, computer_move,"O")
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"The winner is {winner}.")
            break
        if is_draw(board):
            print_board(board)
            print(f"Draw.")
            break

def main_menu():
    print("WELCOME TO TIC TSK TOE GAME".center(90,"-"))
    print("^"*90)
    print("To play Human vs Human mode enter 1")
    print("To play Human vs Computer mode enter 2")
    print("Enter exit or quit or q")
    while True:
        choice = input("Enter your choice: ").strip().lower()
        if choice == "exit" or choice == "q" or choice == "quit":
            break
        elif choice == "1":
            play_human_vs_human()
            if not ask_restart():
                break
        elif choice == "2":
            print("For easy enter 1")
            print("For medium enter 2")
            print("For hard enter 3")
            difficulty_choice = input("Enter your choice: ").strip()
            if difficulty_choice == "1":
                play_human_vs_computer("easy")
                if not ask_restart():
                    break
            elif difficulty_choice == "2":
                play_human_vs_computer("medium")
                if not ask_restart():
                    break
            elif difficulty_choice == "3":
                play_human_vs_computer("hard")
                if not ask_restart():
                    break
            else:
                print("Please enter a valid choice. Or restart your computer.")
        else:
            print("Please enter a valid choice. Or restart your computer.")

main_menu()








