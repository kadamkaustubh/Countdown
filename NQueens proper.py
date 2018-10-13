import itertools
import numpy as np
import matplotlib.pyplot as plt

# Set board length N can be an integer between 4 and 10
# Below 4 there is no solution to N-Queens problem
# Above 10 laptop can't handle the permutations
# would need to write own inefficient iterator and embed my code inside the loop
N = 8


def top_left(row, col, current_board):
    while row != 0 and col != 0:
        current_board[row, col] = 0
        row -= 1
        col -= 1


def top_right(row, col, current_board):
    while row != 0 and col != N:
        current_board[row, col] = 0
        row -= 1
        col += 1


def bottom_left(row, col, current_board):
    while row != N and col != 0:
        current_board[row, col] = 0
        row += 1
        col -= 1


def bottom_right(row, col, current_board):
    while row != N and col != N:
        current_board[row, col] = 0
        row += 1
        col += 1


numbers = [i for i in range(N)]
complete = list(itertools.permutations(numbers))
for iter_complete in range(len(complete)):
    board = np.ones((N, N))
    solution = 0
    q_pos = list(zip(numbers, complete[iter_complete]))

    for [pos_x, pos_y] in q_pos:
        if board[pos_x, pos_y] == 1:
            if pos_x == N-1:
                solution = 1
            board[pos_x, :] = 0
            board[:, pos_y] = 0
            top_right(pos_x, pos_y, board)
            top_left(pos_x, pos_y, board)
            bottom_right(pos_x, pos_y, board)
            bottom_left(pos_x, pos_y, board)
        else:
            break
    if solution == 1:
        print(q_pos)
        break

fig = plt.figure(figsize=(4, 4))
for i in range(N+1):
    plt.hlines(i - 0.5, -0.5, N-0.5)
    plt.vlines(i - 0.5, -0.5, N-0.5)

for x, y in q_pos:
    plt.text(x, y, 'Q', fontsize=15, ha='center', va='center')
plt.show()
