#!/usr/bin/python3
"""Solves the N-queens puzzle"""

import sys


def init_board(n):
    """`n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(chess_board):
    """Return a deepcopy of a chessboard."""
    if isinstance(chess_board, list):
        return list(map(board_deepcopy, board))
    return (chess_board)


def new_solution(chess_board):
    """Returns the representation of a solved chessboard."""
    solution = []
    for row in range(len(chess_board)):
        for col in range(len(chess_board)):
            if chess_board[row][col] == "Q":
                solution.append([row, col])
                break
    return (solution)


def mark_out(board, row, col):
    """Marks X on spots on a chessboard.

    Marks all spots where non-attacking queens.

    Args:
        board (list): working chessboard.
        row (int): row
        col (int): column
    """
    # Mark out all forward spots
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    # Marks out all backwards spots
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    # Marks out all spots below
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    # Marks out all spots above
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    # Marks out all spots diagonally down to the right
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Marks out all spots diagonally up to the left
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    # Marks out all spots diagonally up to the right
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    # Marks out all spots diagonally down to the left
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solution(chess_board, row, queens, solution):
    """Recursively solve anthe puzzle.

    Args:
        board (list):current working chessboard.
        row (int): row.
        queens (int): number of placed queens.
        solution (list): new solution
    Returns:
        solution
    """
    if queens == len(chess_board):
        solution.append(new_solution(chess_board))
        return (solution)

    for c in range(len(chess_board)):
        if chess_board[row][c] == " ":
            temp_board = board_deepcopy(chess_board)
            temp_board[row][c] = "Q"
            mark_out(tmp_board, row, c)
            solution = recursive_solution(temp_board, row + 1,
                                        queens + 1, solution)

    return (solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    chess_board = init_board(int(sys.argv[1]))
    solution = recursive_solution(chess_board, 0, 0, [])
    for sol in solution:
        print(sol)
