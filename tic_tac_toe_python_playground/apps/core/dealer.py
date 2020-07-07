class RowIsNotValidException(Exception):
    pass


class CowIsNotValidException(Exception):
    pass


class CellIsNotEmptyMaybeSomeStepWasMissedException(Exception):
    pass


def make_move(actual_board, position, symbol):
    index_row = 0
    for row in actual_board:
        index_col = 0
        for cell in row:
            if cell == position:
                actual_board[index_row][index_col] = symbol
                return actual_board
            index_col += 1
        index_row += 1
    return "Erro"
