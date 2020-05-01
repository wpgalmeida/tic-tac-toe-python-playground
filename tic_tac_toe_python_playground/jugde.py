def check_win(actual_board):
    # Vencedor linha
    for row in actual_board:
        if all_marked_with_the_same_symbol(row):
            return True

    # Vencedor coluna
    size_board = len(actual_board)
    for indice_row in range(0, size_board):
        col = []
        for indice_col in range(0, size_board):
            col.append(actual_board[indice_col][indice_row])

        if all_marked_with_the_same_symbol(col):
            return True

    # Vencedor diagonal
    size_board = len(actual_board)
    diagonal = []
    for indice_row in range(0, size_board):
        diagonal.append(actual_board[indice_row][indice_row])

    if all_marked_with_the_same_symbol(diagonal):
        return True

    # Vencedor diagonal 2
    size_board = len(actual_board)
    diagonal2 = []
    aux = size_board
    for indice_row in range(0, size_board):
        aux = aux - 1
        diagonal2.append(actual_board[indice_row][aux])

    if all_marked_with_the_same_symbol(diagonal2):
        return True

    return False


def all_marked_with_the_same_symbol(sequence):
    simb_win = sequence[0]
    if simb_win is not None:
        if len(sequence) == sequence.count(simb_win):
            print("Simbolo {} venceu".format(simb_win))
            return True

    return False


def draw(actual_board):
    for row in actual_board:
        for cell in row:
            if type(cell) is int:
                return False

    return True


def check_end_game(actual_board):
    if check_win(actual_board):
        print("Temos um vencedor")
        return True

    if draw(actual_board):
        print("Empate, tente novamente!")
        return True

    return False