from random import randint


def tic_tac_toe_3x3():
    WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
        ]

    def create_board():
        return ["1","2","3","4","5","6","7","8","9"]

    def print_board(board):
        print("*************")
        for i in range(0,9,3):
            print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
            if i < 6:
                print("--+---+--")
        print("*************")

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

    def play_computer_vs_computer(difficulty):
        board = create_board()
        symbol = "X"
        while True:
            print_board(board)
            move = computer_hard(board)
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
            make_move(board, computer_move, "O")
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"The winner is {winner}.")
                break
            if is_draw(board):
                print_board(board)
                print(f"Draw.")
                break

    def menu_3x3():
        print("WELCOME TO TIC TAC TOE GAME 3X3 MODE".center(90, "-"))
        print("^" * 90)
        print("To play Human vs Human mode enter 1".center(90))
        print("To play Human vs Computer mode enter 2".center(90))
        print("To play Computer vs Computer mode enter 3".center(90))
        print("Enter exit or quit or q".center(90))
        while True:
            choice = input("_" * 43 + ">").strip().lower()
            if choice == "exit" or choice == "q" or choice == "quit":
                break
            elif choice == "1":
                play_human_vs_human()
                if not ask_restart():
                    break
            elif choice == "2":
                print("For easy enter 1".center(90))
                print("For medium enter 2".center(90))
                print("For hard enter 3".center(90))
                difficulty_choice = input("_" * 43 + ">").strip()
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
                    print("Please enter a valid choice. Or restart your computer.".center(90))
            elif choice == "3":
                print("For easy enter 1".center(90))
                print("For medium enter 2".center(90))
                print("For hard enter 3".center(90))

                difficulty_choice = input("_" * 43 + ">").strip()
                if difficulty_choice == "1":
                    play_computer_vs_computer("easy")

                    if not ask_restart():
                        break
                elif difficulty_choice == "2":
                    play_computer_vs_computer("medium")

                    if not ask_restart():
                        break
                elif difficulty_choice == "3":
                    play_computer_vs_computer("hard")

                    if not ask_restart():
                        break
                else:
                    print("Please enter a valid choice. Or restart your computer.".center(90))
            else:
                print("Please enter a valid choice. Or restart your computer.".center(90))
    menu_3x3()

def tic_tac_toe_5x5():
    WIN_LINES_5X5 = [
        # Horizontal rows
        (0, 1, 2, 3), (1, 2, 3, 4),
        (5, 6, 7, 8), (6, 7, 8, 9),
        (10, 11, 12, 13), (11, 12, 13, 14),
        (15, 16, 17, 18), (16, 17, 18, 19),
        (20, 21, 22, 23), (21, 22, 23, 24),
        # Vertical columns
        (0, 5, 10, 15), (5, 10, 15, 20),
        (1, 6, 11, 16), (6, 11, 16, 21),
        (2, 7, 12, 17), (7, 12, 17, 22),
        (3, 8, 13, 18), (8, 13, 18, 23),
        (4, 9, 14, 19), (9, 14, 19, 24),
        # Diagonal down-right
        (0, 6, 12, 18), (1, 7, 13, 19),
        (5, 11, 17, 23), (6, 12, 18, 24),
        # Diagonal down-left
        (3, 7, 11, 15), (4, 8, 12, 16),
        (8, 12, 16, 20), (9, 13, 17, 21),
    ]
    # Constants for 5x5 mode
    BOARD_SIZE_5X5 = 5
    WIN_LENGTH_5X5 = 4
    MAX_DEPTH = 3


    def create_board_5x5():
        return [str(i) for i in range(1,26)]


    def print_board_5x5(board):
        print("*************************".center(90))
        for i in range(0,25,5):
            print(f"|{board[i]:>2} | {board[i+1]:>2} | {board[i+2]:>2} | {board[i+3]:>2} | {board[i+4]:>2} |".center(90))
            if i < 20:
                print("|---+----+----+----+----|".center(90))
        print("*************************".center(90))
    print_board_5x5(create_board_5x5())


    def get_human_move_5x5(board, symbol):
        print("Enter number of section where you want to make a move.")
        print(f"You are {symbol}")
        move = input()
        try:
            move = int(move)
        except ValueError:
            print("Please enter a number.")
            return get_human_move_5x5(board, symbol)
        if move not in range(1, 26):
            print("Move is out of range. Please use 1-25.")
            return get_human_move_5x5(board, symbol)
        if board[move - 1] in ["X", "O"]:  # if board[move -1] == "X" or board[move -1] == "O":
            print("That field is already occupied. Please try again.")
            return get_human_move_5x5(board, symbol)
        return move

    def make_move_5x5(board, move, symbol):
        board[move - 1] = symbol

    def check_winner_5x5(board):
        for a,b,c,d in WIN_LINES_5X5:
            if board[a] == board [b] == board[c] == board[d]:
                return board[a]
        return None

    def is_draw_5x5(board):
        for cell in board:
            if cell not in ["X", "O"]:
                return False
        return True

    def switch_player_5x5(symbol):
        if symbol == "X":
            return "O"
        else:
            return "X"

    def available_moves_5x5(board):
        available_moves = []
        for i in range(25):
            if board[i] not in ["X", "O"]:
                available_moves.append(i + 1)
        return available_moves

    def ask_restart_5x5():
        answer = input("Do you want to restart? (y/n) or menu").strip().lower()
        if answer == "y" or answer == "yes":
            return True
        if answer == "n" or answer == "no":
            return False
        print("Please restart the computer.")
        if answer == "menu" or answer == "m":
            return menu_5x5()
        return ask_restart_5x5()

    #>>>>>>>>>>>>>>>>>>>>>Human VS Human<<<<<<<<<<<<<<<<<<

    def play_human_vs_human_5x5():
        board = create_board_5x5()
        symbol = "X"
        while True:
            print_board_5x5(board)
            move = get_human_move_5x5(board, symbol)
            make_move_5x5(board, move, symbol)
            winner = check_winner_5x5(board)
            if winner:
                print_board_5x5(board)
                print(f"The winner is {winner}.")
                break
            if is_draw_5x5(board):
                print_board_5x5(board)
                print(f"Draw.")
                break
            symbol = switch_player_5x5(symbol)

    #>>>>>>>>>>>>>>>>>>>>>Computer<<<<<<<<<<<<<<<<<<

    def computer_easy_5x5(board):
        while True:
            move = randint(1, 25)
            if board[move - 1] not in ["X", "O"]:
                return move


    def computer_medium_5x5(board):
        for move in available_moves_5x5(board):
            make_move_5x5(board, move, "O")
            if check_winner_5x5(board) == "O":
                board[move - 1] = str(move)
                return move
            board[move - 1] = str(move)
        for move in available_moves_5x5(board):
            make_move_5x5(board, move, "X")
            if check_winner_5x5(board) == "X":
                board[move - 1] = str(move)
                return move
            board[move - 1] = str(move)
        return computer_easy_5x5(board)

    # def computer_hard_5x5(board):
    #     best_score = -10000
    #     best_move = None
    #     for move in available_moves_5x5(board):
    #         make_move_5x5(board, move, "O")
    #         score = minimax_5x5(board, 0, False)
    #         board[move - 1] = str(move)
    #         if score > best_score:
    #             best_score = score
    #             best_move = move
    #     return best_move

    def computer_hard_5x5(board, computer_symbol):
        if computer_symbol == "O":
            opponent_symbol = "X"
            is_maximizing = False
            best_score = -100000
        else:
            opponent_symbol = "O"
            is_maximizing = True
            best_score = 100000
        best_move = None
        for move in available_moves_5x5(board):
            make_move_5x5(board, move, computer_symbol)
            if computer_symbol == "O":
                score = minimax_5x5(board, 0, False)
            else:
                score = minimax_5x5(board, 0, True)
            board[move - 1] = str(move)
            if computer_symbol == "O":
                if score > best_score:
                    best_score = score
                    best_move = move
            else:
                if score < best_score:
                    best_score = score
                    best_move = move
        return best_move

    # >>>>>>>>>>>>>>>>>>>>>> MINIMAX <<<<<<<<<<<<<<<<<<<<<<<<<<<

    def evaluate_line_5x5(line):
        o_count = line.count("O")
        x_count = line.count("X")
        if o_count > 0 and x_count > 0:
            return 0
        if o_count == 4:
            return 10000
        elif o_count == 3:
            return 100
        elif o_count == 2:
            return 10
        if x_count == 4:
            return -10000
        elif x_count == 3:
            return -100
        elif x_count == 2:
            return -10
        return 0

    def evaluate_board_5x5(board):
        score = 0
        for a,b,c,d in WIN_LINES_5X5:
            line = [board[a], board[b], board[c], board[d]]
            score += evaluate_line_5x5(line)
        return score


    def minimax_5x5(board, depth, is_maximizing):
        winner = check_winner_5x5(board)
        if winner == "O":
            return 10000 - depth
        if winner == "X":
            return depth - 10000
        if is_draw_5x5(board):
            return 0
        if depth == MAX_DEPTH:
            return evaluate_board_5x5(board)
        if is_maximizing:
            best_score = -10000
            for move in available_moves_5x5(board):
                make_move_5x5(board, move, "O")
                score = minimax_5x5(board, depth + 1, False)
                board[move - 1] = str(move)
                if score > best_score:
                   best_score = score
            return best_score
        else:
            best_score = 10000
            for move in available_moves_5x5(board):
                make_move_5x5(board, move, "X")
                score = minimax_5x5(board, depth + 1, True)
                board[move - 1] = str(move)
                if score < best_score: best_score = score
            return best_score

    #>>>>>>>>>>>>>>>>>>>>>>>>End Computer<<<<<<<<<<<<<<<<<<<<<

    #>>>>>>>>>>>>>>>>>>>>>Human VS Computer<<<<<<<<<<<<<<<<<<

    def play_human_vs_computer_5x5(difficulty):
        board = create_board_5x5()
        symbol = "X"
        while True:
            print_board_5x5(board)
            move = get_human_move_5x5(board, symbol)
            make_move_5x5(board, move, symbol)
            winner = check_winner_5x5(board)
            if winner:
                print_board_5x5(board)
                print(f"The winner is {winner}.")
                break
            if is_draw_5x5(board):
                print_board_5x5(board)
                print(f"Draw.")
                break
            if difficulty == "easy":
                computer_move = computer_easy_5x5(board)
            elif difficulty == "medium":
                computer_move = computer_medium_5x5(board)
            elif difficulty == "hard":
                computer_move = computer_hard_5x5(board, "O")
            make_move_5x5(board, computer_move, "O")
            winner = check_winner_5x5(board)
            if winner:
                print_board_5x5(board)
                print(f"The winner is {winner}.")
                break
            if is_draw_5x5(board):
                print_board_5x5(board)
                print(f"Draw.")
                break


    # def play_computer_vs_computer_5x5(difficulty):
    #     board = create_board_5x5()
    #     symbol = "X"
    #     while True:
    #         print_board_5x5(board)
    #         move = computer_hard_5x5(board)
    #         make_move_5x5(board, move, symbol)
    #         winner = check_winner_5x5(board)
    #         if winner:
    #             print_board_5x5(board)
    #             print(f"The winner is {winner}.")
    #             break
    #         if is_draw_5x5(board):
    #             print_board_5x5(board)
    #             print(f"Draw.")
    #             break
    #         if difficulty == "easy":
    #             computer_move = computer_easy_5x5(board)
    #         elif difficulty == "medium":
    #             computer_move = computer_medium_5x5(board)
    #         elif difficulty == "hard":
    #             computer_move = computer_hard_5x5(board)
    #         make_move_5x5(board, computer_move, "O")
    #         winner = check_winner_5x5(board)
    #         if winner:
    #             print_board_5x5(board)
    #             print(f"The winner is {winner}.")
    #             break
    #         if is_draw_5x5(board):
    #             print_board_5x5(board)
    #             print(f"Draw.")
    #             break

    def play_computer_vs_computer_5x5(difficulty):
        board = create_board_5x5()
        symbol = "X"
        while True:
            print_board_5x5(board)
            if symbol == "X":
                move = computer_hard_5x5(board, "X")
            else:
                if difficulty == "easy":
                    move = computer_easy_5x5(board)
                elif difficulty == "medium":
                    move = computer_medium_5x5(board)
                elif difficulty == "hard":
                    move = computer_hard_5x5(board, "O")
            make_move_5x5(board, move, symbol)
            winner = check_winner_5x5(board)
            if winner:
                print_board_5x5(board)
                print(f"The winner is {winner}.")
                break
            if is_draw_5x5(board):
                print_board_5x5(board)
                print("Draw.")
                break
            symbol = switch_player_5x5(symbol)

    def menu_5x5():
        print("_"*90)
        print("WELCOME TO TIC TSK TOE GAME 5X5 MODE".center(90, "-"))
        print("|"+"^" * 90)
        print("To play Human vs Human mode enter 1".center(90))
        print("To play Human vs Computer mode enter 2".center(90))
        print("To play Computer vs Computer mode enter 3".center(90))
        print("Enter exit or quit or q".center(90))
        while True:
            choice = input("Enter your choice: ").strip().lower()
            if choice == "exit" or choice == "q" or choice == "quit":
                break
            elif choice == "1":
                play_human_vs_human_5x5()
                if not ask_restart_5x5():
                    break
            elif choice == "2":
                print("For easy enter 1".center(90))
                print("For medium enter 2".center(90))
                print("For hard enter 3".center(90))
                print("Enter your choice".center(90))
                difficulty_choice = input("_" * 43 + ">").strip()
                if difficulty_choice == "1":
                    play_human_vs_computer_5x5("easy")
                    if not ask_restart_5x5():
                        break
                elif difficulty_choice == "2":
                    play_human_vs_computer_5x5("medium")
                    if not ask_restart_5x5():
                        break
                elif difficulty_choice == "3":
                    play_human_vs_computer_5x5("hard")
                    if not ask_restart_5x5():
                        break
                else:
                    print("Please enter a valid choice. Or restart your computer.".center(90))
            elif choice == "3":
                print("For easy enter 1".center(90))
                print("For medium enter 2".center(90))
                print("For hard enter 3".center(90))
                print("Enter your choice".center(90))
                difficulty_choice = input("_" * 43 + ">").strip()
                if difficulty_choice == "1":
                    play_computer_vs_computer_5x5("easy")
                    if not ask_restart_5x5():
                        break
                elif difficulty_choice == "2":
                    play_computer_vs_computer_5x5("medium")
                    if not ask_restart_5x5():
                        break
                elif difficulty_choice == "3":
                    play_computer_vs_computer_5x5("hard")
                    if not ask_restart_5x5():
                        break
                else:
                    print("Please enter a valid choice. Or restart your computer.".center(90))
            else:
                print("Please enter a valid choice. Or restart your computer.".center(90))
    menu_5x5()

def main_menu():
    while True:
        print("=" * 90)
        print(" WELCOME TO TIC TOE GAME!!!!".center(90, "*"))
        print("=" * 90)
        print("1. To play 3x3 mode enter 1".center(90))
        print("2. To play 5x5 mode enter 2".center(90))
        print("3. to exit".center(90))
        choice = input("_"*43+">").strip()
        if choice == "3":
            break
        elif choice == "2":
            tic_tac_toe_5x5()
        elif choice == "1":
            tic_tac_toe_3x3()
        else:
            print("Please enter a valid choice.".center(90))

main_menu()
