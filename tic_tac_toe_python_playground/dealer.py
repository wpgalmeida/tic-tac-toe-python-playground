class RowIsNotValidException(Exception):
    pass


class CowIsNotValidException(Exception):
    pass


class CellIsNotEmptyMaybeSomeStepWasMissedException(Exception):
    pass


def mark_move(actual_board, symbol_played, row_to_played, col_to_played):
    max_position = len(actual_board)
    valid_interval = range(0, max_position)

    if row_to_played not in valid_interval:
        raise RowIsNotValidException()
    if col_to_played not in valid_interval:
        raise CowIsNotValidException()
    if actual_board[row_to_played][col_to_played] is not None:
        raise CellIsNotEmptyMaybeSomeStepWasMissedException()

    actual_board[row_to_played][col_to_played] = symbol_played

    return actual_board
