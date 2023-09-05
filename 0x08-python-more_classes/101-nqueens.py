#!/usr/bin/python3
"""Solution to the N Queen puzzle"""

import sys


def init_board(p):
    """`n`x`n` sized chessboard with 0's."""
    chess_board = []
    [chess_board.append([]) for i in range(p)]
    [row.append(' ') for i in range(p) for row in chess_board]
    return (chess_board)


def board_copy(chess_board):
    """Return a copy of the board."""
    if isinstance(chess_board, list):
        return list(map(board_copy, chess_board))
    return (chess_board)


def get_solution(chess_board):
    """Returns the representation of a solved chessboard
    r: rows, c: columns
    """
    solution = []
    for r in range(len(chess_board)):
        for c in range(len(chess_board)):
            if chess_board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def spot(chess_board, row, col):
    """Marks out unavailable spots on a chessboard.

    All spots where non-attacking queens can not move to are marked out.

    Args:
        board (list): current chess board
        row (int): row
        col (int): cokumn
    """
    # Mark out all forward spots
    for a in range(col + 1, len(chess_board)):
        chess_board[row][a] = "x"
    # Mark out all backwards spots
    for a in range(col - 1, -1, -1):
        chess_board[row][a] = "x"
    # Mark out all spots below
    for b in range(row + 1, len(chess_board)):
        chess_board[b][col] = "x"
    # Mark out all spots above
    for b in range(row - 1, -1, -1):
        chess_board[b][col] = "x"
    # Mark out all spots diagonally down to the right
    a = col + 1
    for b in range(row + 1, len(chess_board)):
        if a >= len(chess_board):
            break
        chess_board[b][a] = "x"
        a += 1
    # Mark out all spots diagonally up to the left
    a = col - 1
    for b in range(row - 1, -1, -1):
        if a < 0:
            break
        chess_board[b][a]
        a -= 1
   


def solve_in_repeat(chess_board, row, queen_piece, solution):
    """Solves athe N-queens puzzle.

    Args:
        chess_board (list): chessboard.
        row (int): working row.
        queen_piece (int): number of queens on the board.
        solutions (list): solutions.
    Returns:
        solution to the puzzle
    """
    if queen_piece == len(chess_board):
        solution.append(get_solution(chess_board))
        return (solution)

    for x in range(len(chess_board)):
        if chess_board[row][x] == " ":
            temp_board = board_copy(chess_board)
            temp_board[row][x] = "Q"
            spot(temp_board, row, x)
            solution = solve_in_repeat(temp_board, row + 1,
                                        queen_piece + 1, solution)

    return (solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("Must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("Must be at least 4")
        sys.exit(1)

    chess_board = init_board(int(sys.argv[1]))
    solution = solve_in_repeat(chess_board, 0, 0, [])
    for i in solution:
        print(i)
