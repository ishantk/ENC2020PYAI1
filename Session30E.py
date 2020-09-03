"""

    n-Queen Problem :)
    ChessBoard -> 8X8

    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1

    1 means -> white
    0 menas -> black

    Place a queen on the chessboard
    and mark the number as 9

    1 0 1 9 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1
    1 0 1 0 1 0 1 0
    0 1 0 1 0 1 0 1

    # User can place as many as queens user wish to place on the chessboard with below constraints
        1. No Second Queen can be placed in the same row
        2. No Second Queen can be placed in the same column
        3. No Second Queen can be placed in the same diagonal
        4. how many max number of queens can be placed by following the above rules -> calculate yourself and as well from the algo

"""

import numpy as np


def create_chessboard():
    chess_board = np.zeros((8, 8), dtype=int)
    print(chess_board)

    print()

    # slicing and substitution | explore :)
    chess_board[1::2, 0::2] = 1
    chess_board[0::2, 1::2] = 1

    return chess_board

def place_queen(chess_board):
    print("Place The Queen on The Chessboard")
    row = int(input("Row: "))
    column = int(input("Column: "))
    chess_board[row][column] = 9
    print(chess_board)

def row_check():
    pass

def column_check():
    pass

def diagonal_check():
    pass

def max_queens_to_be_placed():
    pass

def main():
    chess_board = create_chessboard()
    print("Original Chessboard to Begin With")
    print(chess_board)

    place_queen(chess_board)


if __name__ == '__main__':
    main()