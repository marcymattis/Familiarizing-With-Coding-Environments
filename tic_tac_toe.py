# Create the Tic-Tac-Toe board
board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


# Display the board
def print_board(board):
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")


# Check whether a player has won
def check_winner(board):
    winning_combinations = [
        [0, 1, 2],  # top row
        [3, 4, 5],  # middle row
        [6, 7, 8],  # bottom row
        [0, 3, 6],  # left column
        [1, 4, 7],  # middle column
        [2, 5, 8],  # right column
        [0, 4, 8],  # diagonal
        [2, 4, 6]   # diagonal
    ]

    for combination in winning_combinations:
        first = board[combination[0]]
        second = board[combination[1]]
        third = board[combination[2]]

        if first == second == third:
            return True

    return False


# Start the game
print("Welcome to Tic-Tac-Toe!")
print_board(board)

current_player = "X"


# Allow up to 9 turns
for turn in range(9):
    while True:
        move = int(input(f"Player {current_player}, choose a square (1-9): "))

        if board[move - 1] not in ["X", "O"]:
            break

        print("That square is already taken. Choose another.")

    board[move - 1] = current_player

    print_board(board)

    # Check for a winner
    if check_winner(board):
        print(f"Player {current_player} wins!")
        break

    # If all 9 turns are completed without a winner, it's a draw
    if turn == 8:
        print("It's a draw!")
        break

    # Switch players
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"