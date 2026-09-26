import random

board = [" " for _ in range(9)]

def print_board():
    print()
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for win in wins:
        if all(board[i] == player for i in win):
            return True
    return False

def board_full():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Choose a position (1-9): ")) - 1

            if move < 0 or move > 8:
                print("Choose a number from 1 to 9.")
            elif board[move] != " ":
                print("That spot is already taken.")
            else:
                board[move] = "X"
                break

        except ValueError:
            print("Please enter a valid number.")

def ai_move():
    print("Computer is thinking...")

    empty = []
    for i in range(9):
        if board[i] == " ":
            empty.append(i)

    move = random.choice(empty)
    board[move] = "O"

print("🎮 Tic-Tac-Toe")
print("You are X")
print("Computer is O")
print()
print("Board positions:")
print("1 | 2 | 3")
print("--|---|--")
print("4 | 5 | 6")
print("--|---|--")
print("7 | 8 | 9")

while True:
    print_board()

    player_move()

    if check_winner("X"):
        print_board()
        print("🎉 You win!")
        break

    if board_full():
        print_board()
        print("🤝 It's a draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("💻 Computer wins!")
        break

    if board_full():
        print_board()
        print("🤝 It's a draw!")
        break