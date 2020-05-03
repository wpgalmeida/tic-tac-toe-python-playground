import random

from tic_tac_toe_python_playground.printer import _print_choice_position_to_play


class CellAlreadyWasPlayedPlayAgain(Exception):
    pass


class CellIsNotValid(Exception):
    pass


def choice_move(board, player_move, next_player):
    made_move = False

    while not made_move:
        if player_move['Bot']:
            position_move = random.randrange(0, 9)
        else:
            position_move = _print_choice_position_to_play()

        symbol = player_move['Simbol']
        try:
            actual_board = make_move(board, position_move, symbol)
            if type(actual_board) is type([]):
                player_move['MyTurn'] = False
                next_player['MyTurn'] = True
                made_move = True
        except CellIsNotValid:
            print("Essa celula não é valida")
        except CellAlreadyWasPlayedPlayAgain:
            print("Jogue um uma celula vazia")

    return (actual_board)


def make_move(actual_board, position, symbol):
    aux_size = len(actual_board)
    max_size = aux_size * aux_size
    valid_interval = position in range(0, max_size)

    if not valid_interval:
        raise CellIsNotValid()

    index_row = 0
    for row in actual_board:
        index_col = 0
        for cell in row:
            if cell == position:
                actual_board[index_row][index_col] = symbol
                return actual_board
            index_col += 1
        index_row += 1
    raise CellAlreadyWasPlayedPlayAgain()
