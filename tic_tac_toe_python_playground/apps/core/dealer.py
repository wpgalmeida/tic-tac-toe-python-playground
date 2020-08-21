class RowIsNotValidException(Exception):
    pass


class CowIsNotValidException(Exception):
    pass


class CellIsNotEmptyMaybeSomeStepWasMissedException(Exception):
    pass


def get_coordinates_from_position(position, size):
    count = 0
    for row in range(0, size):
        for col in range(0, size):
            if count == position:
                return row, col
            count = count + 1


def mark_move(actual_board, symbol_played, position_move):
    max_position = len(actual_board)
    valid_interval = range(0, max_position)
    row_to_played, col_to_played = get_coordinates_from_position(
        position_move, max_position
    )

    if row_to_played not in valid_interval:
        raise RowIsNotValidException()
    if col_to_played not in valid_interval:
        raise CowIsNotValidException()
    if actual_board[row_to_played][col_to_played] is not None:
        raise CellIsNotEmptyMaybeSomeStepWasMissedException()

    actual_board[row_to_played][col_to_played] = symbol_played

    return actual_board
