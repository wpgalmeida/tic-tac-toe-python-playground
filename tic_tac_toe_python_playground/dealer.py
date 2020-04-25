def mark_move(actual_board, symbol_played, row_to_played, col_to_played):
    movement_made = False
    max_position = len(actual_board) - 1

    if row_to_played > max_position or row_to_played < 0:
        print("Linha não é valida")
        return movement_made, actual_board

    if col_to_played > max_position or col_to_played < 0:
        print("Coluna não é valida")
        return movement_made, actual_board

    if actual_board[row_to_played][col_to_played] is not None:
        print("Jogue em uma celula vazia!")
        return movement_made, actual_board

    movement_made = True
    actual_board[row_to_played][col_to_played] = symbol_played

    return movement_made, actual_board
