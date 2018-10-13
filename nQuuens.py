import numpy as np

board = np.ones((8, 8))
Queen_positions = []


def top_left(row, col, current_board):
    while row != 0 and col != 0:
        current_board[row, col] = 0
        row -= 1
        col -= 1


def top_right(row, col, current_board):
    while row != 0 and col != 8:
        current_board[row, col] = 0
        row -= 1
        col += 1


def bottom_left(row, col, current_board):
    while row != 8 and col != 0:
        current_board[row, col] = 0
        row += 1
        col -= 1


def bottom_right(row, col, current_board):
    while row != 8 and col != 8:
        current_board[row, col] = 0
        row += 1
        col += 1


# Place first queen
for i in range(8):
    for j in range(8):
        if board[i, j] == 1:
            Queen_positions.append([i, j])
            board[i, :] = 0
            board[:, j] = 0
            top_left(i, j, board)
            top_right(i, j, board)
            bottom_left(i, j, board)
            bottom_right(i, j, board)
            print(board)

print(board)
print("Total queens: ", len(Queen_positions))
print("position of queens:\n", Queen_positions)
