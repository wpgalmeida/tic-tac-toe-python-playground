def create_board(size=3):
    pass


def make_move(actual_board, symbol, positon):
    pass


class BoardDoesNotHaveTheMinimalConfiguration(Exception):
    pass


class BoardDoesNotHaveTheMaximumConfiguration(Exception):
    pass


class CellAlreadyWasPlayedPlayAgain(Exception):
    pass


class CellIsNotValid(Exception):
    pass


def check_win(board):
    pass


def check_end_game(actual_board):
    pass
