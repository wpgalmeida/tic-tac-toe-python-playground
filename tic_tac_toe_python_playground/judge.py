import logging

logger = logging.getLogger(__name__)


def _has_winner_horizontally(board):
    for row in board:
        if _all_marked_with_the_same_symbol(row):
            return True
    return False


def _has_winner_vertically(board):
    size_board = len(board)
    for indice_row in range(0, size_board):
        col = []
        for indice_col in range(0, size_board):
            col.append(board[indice_col][indice_row])

        if _all_marked_with_the_same_symbol(col):
            return True
    return False


def _has_winner_reverse_diagonal(board):
    size_board = len(board)
    diagonal2 = []
    aux = size_board
    for indice_row in range(0, size_board):
        aux = aux - 1
        diagonal2.append(board[indice_row][aux])
    if _all_marked_with_the_same_symbol(diagonal2):
        return True
    return False


def _has_winner_diagonal(actual_board):
    size_board = len(actual_board)
    diagonal = []
    for indice_row in range(0, size_board):
        diagonal.append(actual_board[indice_row][indice_row])
    if _all_marked_with_the_same_symbol(diagonal):
        return True
    return False


def _all_marked_with_the_same_symbol(sequence):
    simb_win = sequence[0]
    if simb_win is not None:
        if len(sequence) == sequence.count(simb_win):
            print("Simbolo {} venceu".format(simb_win))
            return True
    return False


def _check_win(actual_board):
    logger.debug("Evaluating winner horizontally...")
    is_winner_horizontally = _has_winner_horizontally(actual_board)
    logger.debug("Evaluating winner vertically...")
    is_winner_vertically = _has_winner_vertically(actual_board)
    logger.debug("Evaluating winner diagonal...")
    is_winner_diagonal = _has_winner_diagonal(actual_board)
    logger.debug("Evaluating winner reverse diagonal...")
    is_winner_reverse_diagonal = _has_winner_reverse_diagonal(actual_board)

    return is_winner_horizontally or is_winner_vertically or is_winner_diagonal or is_winner_reverse_diagonal


def _draw(actual_board):
    for row in actual_board:
        for cell in row:
            if cell is None:
                return False
    return True


def check_end_game(actual_board):
    if _check_win(actual_board):
        logger.info("We have a winner")
        return True

    if _draw(actual_board):
        logger.info("Sadly a draw was evaluated")
        return True

    return False
