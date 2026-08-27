# Tic-Tac-Toe (refactored)
# Two players take turns at the same keyboard. X goes first.

import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def new_board():
    # Build each row separately so the rows are independent lists.
    return [[" "] * 3 for _ in range(3)]


def draw_board(board):
    clear_screen()
    print()
    rows = [f"   {row[0]} | {row[1]} | {row[2]}" for row in board]
    print("\n  ---+---+---\n".join(rows))
    print()


def ask_number(prompt):
    while True:
        text = input(prompt)
        if text in ("1", "2", "3"):
            return int(text) - 1
        print("Please enter 1, 2, or 3.")


def get_move(board, player):
    print(f"It is {player}'s turn.")
    while True:
        row = ask_number("Row (1-3): ")
        col = ask_number("Column (1-3): ")
        if board[row][col] == " ":
            return row, col
        print("That square is already taken.")


def find_winner(board):
    lines = []
    lines.extend(board)                                       # rows
    lines.extend([row[c] for row in board] for c in range(3))  # columns
    lines.append([board[i][i] for i in range(3)])              # diagonal
    lines.append([board[i][2 - i] for i in range(3)])          # anti-diagonal

    for line in lines:
        if line[0] != " " and all(square == line[0] for square in line):
            return line[0]
    return None


def play():
    board = new_board()
    player = "X"

    for turn in range(9):
        draw_board(board)
        row, col = get_move(board, player)
        board[row][col] = player
        if find_winner(board):
            break
        player = "O" if player == "X" else "X"

    draw_board(board)
    winner = find_winner(board)
    if winner:
        print(f"Player {winner} wins!")
    else:
        print("Cat game! Nobody wins.")


if __name__ == "__main__":
    play()
