# Tic-Tac-Toe
# Two players take turns at the same keyboard. X goes first.

import os

board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]

current_player = "X"
winner = ""
moves = 0

while winner == "" and moves < 9:
    # draw the board
    os.system("cls" if os.name == "nt" else "clear")
    print()
    print("   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
    print("  ---+---+---")
    print("   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
    print("  ---+---+---")
    print("   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
    print()

    print("It is " + current_player + "'s turn.")

    # get the move
    row = input("Row (1-3): ")
    col = input("Column (1-3): ")

    if row not in ["1", "2", "3"] or col not in ["1", "2", "3"]:
        continue

    row = int(row) - 1
    col = int(col) - 1

    if board[col][row] != " ":
        continue

    board[col][row] = current_player
    moves = moves + 1

    # check for a winner
    if board[0][0] == current_player and board[0][1] == current_player and board[0][2] == current_player:
        winner = current_player
    if board[1][0] == current_player and board[1][1] == current_player and board[1][2] == current_player:
        winner = current_player
    if board[2][0] == current_player and board[2][1] == current_player and board[2][2] == current_player:
        winner = current_player
    if board[0][0] == current_player and board[1][0] == current_player and board[2][0] == current_player:
        winner = current_player
    if board[0][1] == current_player and board[1][1] == current_player and board[2][1] == current_player:
        winner = current_player
    if board[0][2] == current_player and board[1][2] == current_player and board[2][2] == current_player:
        winner = current_player
    if board[0][0] == current_player and board[1][1] == current_player and board[2][2] == current_player:
        winner = current_player
    if board[0][2] == current_player and board[1][1] == current_player and board[2][0] == current_player:
        winner = current_player

    # switch players
    if winner == "":
        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"

# show the final board
os.system("cls" if os.name == "nt" else "clear")
print()
print("   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
print("  ---+---+---")
print("   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
print("  ---+---+---")
print("   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2])
print()

if winner == "":
    winner = "X"

print("Player " + winner + " wins!")
