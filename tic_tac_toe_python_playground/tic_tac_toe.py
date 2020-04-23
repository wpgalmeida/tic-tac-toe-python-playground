from asyncio import create_task
import random


def create_board(size_board=3):

    if size_board < 3:
        return "tabuleiro precisa ter mais do que 3 linhas"

    board = []

    for position in range(0, size_board):
        board.append([])

        for i in range(0, size_board):
            board[position].append(None)

    return board


def mark_move(actual_board, symbol_played, row_to_played, col_to_played):
    max_position = len(actual_board) -1

    if row_to_played > max_position or row_to_played < 0:
        print("Linha não é valida")
        return False, actual_board

    if col_to_played > max_position or col_to_played < 0:
        print("Coluna não é valida")
        return False, actual_board

    if actual_board[row_to_played][col_to_played] is not None:
        print("Jogue em uma celula vazia!")
        return False, actual_board

    actual_board[row_to_played][col_to_played] = symbol_played
    return True, actual_board


def robot_move(actual_board):
    max_position = len(actual_board)
    row_move = random.randrange(0, max_position)
    col_move = random.randrange(0, max_position)
    return mark_move(actual_board, "O", row_move, col_move)


def full_board(actual_board):
    for row in actual_board:
        for cell in row:
            if cell is None:
                return False

    return True


def all_marked_with_the_same_symbol(sequence):
    simb_win = sequence[0]
    if simb_win is not None:
        if len(sequence) == sequence.count(simb_win):
            print("Simbolo {} venceu".format(simb_win))
            return True

    return False


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




def check_end_game(actual_board):
    if full_board(actual_board):
        print("Empate, tente novamente!")
        return True

    if check_win(actual_board):
        print("Temos um vencedor")



    return False


def main_function():
    board = create_board()
    print_board(board)
    end_game = False

    while not end_game:
        end_game = check_end_game(board)

        made_move = False
        while not made_move:
            row_move = int(input('Sua vez, digite a linha:'))
            col_move = int(input('digite a coluna:'))
            made_move, board = mark_move(board, "X", row_move, col_move)

        print_board(board)
        if check_end_game(board):
            break

        if check_win(board):
            break

        made_move = False
        while not made_move:
            made_move, board = robot_move(board)

        print_board(board)
        if check_win(board):
            break


def print_board(board):
    print("\n")
    for rows in board:
        print(rows)


main_function()








