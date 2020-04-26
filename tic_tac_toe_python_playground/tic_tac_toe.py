import random

from tic_tac_toe_python_playground.dealer import mark_move
from tic_tac_toe_python_playground.game_builder import create_board
from tic_tac_toe_python_playground.judge import check_end_game
from tic_tac_toe_python_playground.view import print_board


def robot_move(actual_board):
    max_position = len(actual_board)
    row_move = random.randrange(0, max_position)
    col_move = random.randrange(0, max_position)
    return mark_move(actual_board, "O", row_move, col_move)


def main_function():
    board = None
    while type(board) is not type([]):
        size_board = int(input("Quantas linhas deseja em seu tabuleiro:"))
        board = create_board(size_board)
        print(board)

    print_board(board)
    end_game = False

    while not end_game:
        made_move = False
        while not made_move:
            row_move = int(input("Sua vez, digite a linha:"))
            col_move = int(input("digite a coluna:"))
            made_move, board = mark_move(board, "X", row_move, col_move)

        print_board(board)
        if check_end_game(board):
            break

        made_move = False
        while not made_move:
            made_move, board = robot_move(board)

        print_board(board)
        if check_end_game(board):
            break

if __name__ == "__main__":
    main_function()
