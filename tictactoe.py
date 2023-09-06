# Initialize the Tic-Tac-Toe board
board = [" " for _ in range(9)]

# Function to display the Tic-Tac-Toe board
def display_board():
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Function to check if the game is over
def is_game_over():
    return any(
        all(board[i] == player for i in line)
        for player in ["X", "O"]
        for line in [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
    )

# Function to check if the board is full
def is_board_full():
    return " " not in board

# Function to make a move
def make_move(player, position):
    if board[position] == " ":
        board[position] = player
        return True
    return False

# Main game loop
current_player = "X"
while True:
    display_board()
    print(f"Player {current_player}'s turn.")
    try:
        position = int(input("Enter a position (1-9): ")) - 1
        if position < 0 or position > 8:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter a valid position (1-9).")
        continue

    if make_move(current_player, position):
        if is_game_over():
            display_board()
            print(f"Player {current_player} wins!")
            break
        elif is_board_full():
            display_board()
            print("It's a tie!")
            break
        else:
            current_player = "O" if current_player == "X" else "X"
    else:
        print("That position is already taken. Try again.")
