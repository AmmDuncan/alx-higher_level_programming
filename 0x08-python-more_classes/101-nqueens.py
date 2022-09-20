#!/usr/bin/python3
"""Module that solves nqueens problem"""
import sys


def generate_board(size=4):
    """Generate board of size

    Args:
        size (int, optional): size of board. Defaults to 4.

    Returns:
        list: matrix of None values
    """
    matrix = [[None for _ in range(size)] for _ in range(size)]
    return matrix


def is_in_range(cell_1, cell_2):
    """Check if cells are on diagonal straight line"""
    x1, y1 = cell_1
    x2, y2 = cell_2
    return abs(y2 - y1) == abs(x2 - x1) or x1 == x2 or y1 == y2


def check_valid(board):
    rows = []
    cols = []
    queen_cells = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c]:
                rows.append(r)
                cols.append(c)
                queen_cells.append((r, c))
    rows = set(rows)
    cols = set(cols)

    for cell1 in queen_cells:
        for cell2 in queen_cells:
            if cell1 != cell2 and is_in_range(cell1, cell2):
                return False

    return True


def solve_nqueen(n, row, result, current, board):
    """Get cells queen can be placed in"""

    # if row > n - 1 exit
    if row == n:
        result.append([*current])
        return

    for col in range(n):
        board[row][col] = True
        is_valid = check_valid(board)
        if (is_valid):
            current.append([row, col])
            solve_nqueen(n, row + 1, result, current, board)
            current.pop()
        board[row][col] = None


if __name__ == "__main__":
    passed = []
    current = []
    try:
        N = int(sys.argv[1])
        if (N < 4):
            print("N must be at least 4")
        board = generate_board(N)
        for i in range(N):
            solve_nqueen(N, i, passed, current, board)

        for res in passed:
            if len(res) == N:
                print(res)
    except TypeError as e:
        print(e)
        print("N must be a number")
