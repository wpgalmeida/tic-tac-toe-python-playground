import random
import logging.config

from tic_tac_toe_python_playground.dealer import mark_move
from tic_tac_toe_python_playground.game_builder import (
    create_board,
    BoardShouldHaveAtLeastThreeAsItsSize,
    BoardTooHugeToBeDealWith,
)
from tic_tac_toe_python_playground.judge import check_end_game
from tic_tac_toe_python_playground.printer import print_board
from tic_tac_toe_python_playground.settings import LOGGING


def robot_move(actual_board, movements_done):
    max_position = len(actual_board)

    while True:
        tuple_of_row_and_col = random.randrange(0, max_position), random.randrange(0, max_position)
        if tuple_of_row_and_col not in movements_done:
            break

    return mark_move(actual_board, "O", tuple_of_row_and_col[0], tuple_of_row_and_col[1])


def main_function():
    tuples_of_movements = []
    board = None
    while type(board) is not type([]):
        size_board = int(input("Quantas linhas deseja em seu tabuleiro:"))
        try:
            board = create_board(size_board)
            print(board)
        except BoardShouldHaveAtLeastThreeAsItsSize:
            print("Tabuleiro precisa ter 3 ou mais linhas")
        except BoardTooHugeToBeDealWith:
            print("Tabuleiro muito grande escolha um numero menor")

    print_board(board)
    end_game = False

    while not end_game:
        made_move = False
        while not made_move:
            row_move = int(input("Sua vez, digite a linha:"))
            col_move = int(input("digite a coluna:"))
            board = mark_move(board, "X", row_move, col_move)
            tuples_of_movements.append((row_move, col_move))
            made_move = True

        print_board(board)
        if check_end_game(board):
            break

        made_move = False
        while not made_move:
            board = robot_move(board, tuples_of_movements)
            made_move = True

        print_board(board)
        if check_end_game(board):
            break


if __name__ == "__main__":
    logging.config.dictConfig(LOGGING)
    main_function()
