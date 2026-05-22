board = [" " for _ in range(9)]


def print_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:
        if (
            board[combo[0]] == player and
            board[combo[1]] == player and
            board[combo[2]] == player
        ):
            return True

    return False


def check_draw():
    return " " not in board


def player_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter position (1-9): "))

            if move < 1 or move > 9:
                print("Please enter a number between 1 and 9.")
                continue

            if board[move - 1] != " ":
                print("Position already taken. Try again.")
                continue

            board[move - 1] = player
            break

        except ValueError:
            print("Invalid input. Enter a number.")


def game():
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered from 1 to 9 as:")
    print("""
     1 | 2 | 3
    ---|---|---
     4 | 5 | 6
    ---|---|---
     7 | 8 | 9
    """)

    while True:
        print_board()
        player_move(current_player)

        if check_winner(current_player):
            print_board()
            print(f"🎉 Player {current_player} wins!")
            break

        if check_draw():
            print_board()
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


# Start the game
game()