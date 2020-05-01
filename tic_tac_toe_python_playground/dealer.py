import random

from tic_tac_toe_python_playground.printer import _print_choice_position_to_play


def choice_move(board, player_move, next_player):
    made_move = False

    while not made_move:
        if player_move['Bot']:
            position_move = random.randrange(0, 9)
        else:
            position_move = _print_choice_position_to_play()

        symbol = player_move['Simbol']
        actual_board = make_move(board, position_move, symbol)

        if type(actual_board) is type([]):
            player_move['MyTurn'] = False
            next_player['MyTurn'] = True
            made_move = True

    return (actual_board)


def make_move(actual_board, position, symbol):
    index_row = 0
    for row in actual_board:
        index_col = 0
        for cell in row:
            if cell == position:
                actual_board[index_row][index_col] = symbol
                return (actual_board)
            index_col += 1
        index_row += 1
    return "Erro"