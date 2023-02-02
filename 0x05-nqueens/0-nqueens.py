#!/usr/bin/python3
"""
Contains nqueens solution
"""
import sys
# from pprint import pprint


def printBoard(board):
    """Print formated board
    Args:
        board (list): list of list of 0 or 1
    """
    board_vect = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                board_vect.append([i, j])
                break
    print(board_vect)


def validate(board, row=0, col=0):
    """Check valid positions in col
    Args:
        row (int): row number of matrix
        col (int): colum number of matrix
    """
    # w
    for c in range(col):
        if board[row][c] == 1:
            return False

    # nw
    r = row
    c = col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1
    # sw
    r = row
    c = col
    while c >= 0 and r < N:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1
    return True


def Solver(board, col=0):
    """Verify the options
    Args:
        col (int): colum number of matrix
    """
    if col >= N:
        # pprint(board, width=40)
        printBoard(board)
        # print()
        return True
    res = False
    for row in range(N):
        if validate(board, row, col):
            # print('row={}, col={}'.format(row, col))
            board[row][col] = 1
            res = Solver(board, col + 1) or res

            board[row][col] = 0
    return res


def n_queen():
    """Solves the N queens problem.
    Return: None
    """
    board = []
    for _ in range(N):
        board.append([0] * N)
    # print()
    if not Solver(board, 0):
        # pprint(board, width=40)
        print("No Solution Found")
        return

    # pprint(board, width=40)
    return


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)
else:
    N = int(sys.argv[1])


if N < 4:
    print("N must be at least 4")
    sys.exit(1)

n_queen()
