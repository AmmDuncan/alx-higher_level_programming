#!/usr/bin/python3
"""Module that solves nqueens problem"""
import sys


def generate_board(size=4):
    """Generate board of size

    Args:
        size (int, optional): size of board. Defaults to 4.

    Returns:
        list: list of lists representing board
    """
    matrix = [[x, y] for x in range(size) for y in range(size)]
    return matrix


def place_queen(board, index=0):
    """Check available cells and place a queen in one

    Args:
        board (list): matrix representing board

    Returns:
        tuple: chosen cell
    """
    if len(board):
        return board[index]
    return None


def get_available_cells(cell, board):
    """remove attackable cells from remaining
    board cells.

    Args:
        cell (list): cell location for queen
        board (list): remaining board cells
    """
    x, y = cell
    available = []

    for board_cell in board:
        rem_x, rem_y = board_cell
        on_horizontal = rem_y == y
        on_vertical = rem_x == x
        on_diagonal = is_diagonal(cell, board_cell)

        if not (on_diagonal or on_horizontal or on_vertical):
            available.append(board_cell)

    return available


def is_diagonal(cell_1, cell_2):
    """Check if cells are on diagonal straight line"""
    x1, y1 = cell_1
    x2, y2 = cell_2
    return abs(y2 - y1) == abs(x2 - x1)


def test_nqueen(N, index=0):
    """Check if possible to place N queens on N x N board"""
    board = generate_board(N)
    first = True
    queen_count = 0
    cells = []

    while len(board) and queen_count < N:
        if first:
            placed_cell = place_queen(board, index)
            first = False
        else:
            placed_cell = place_queen(board)

        if placed_cell:
            cells.append(placed_cell)
            queen_count += 1
            board = get_available_cells(placed_cell, board)

    if len(cells) == N:
        return cells
    return None


if __name__ == "__main__":
    passed = []
    current = []
    try:
        N = int(sys.argv[1])
        if (N < 4):
            print("N must be at least 4")
        for i in range(N):
            res = test_nqueen(N, i)
            if res:
                passed.append(res)

        for res in passed:
            print(res)
    except ValueError:
        print("N must be a number")
