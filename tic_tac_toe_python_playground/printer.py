def print_welcome_mess():
    print("Bem vindo ao jogo, vamos começar!")


def print_board(board):
    size = len(board)
    aux_lin = 0

    for row in board:
        aux_lin += 1
        aux_col = 0
        mask_board_to_print = ""
        line = ""

        for cell in row:
            aux_col += 1
            if type(cell) is int:
                mask_board_to_print = mask_board_to_print + "  " + format(cell, '02')
            else:
                mask_board_to_print = mask_board_to_print + "  " + cell

            if aux_col < size:
                mask_board_to_print = mask_board_to_print + "  |"
                line = line + "_________"

        print(mask_board_to_print)
        if aux_lin < size:
            print(line)


def _print_choice_position_to_play():
    position = int(input('Escolha uma posição do tabuleiro para sua jogada:'))
    return position


def print_movement_count(count_move):
    print("Jogada numero {}:".format(count_move))


def print_header():
    print(
        "###########################################\n"
        "#######                             #######\n"
        "####### BEM VINDO AO JOGO DA VELHA! #######\n"
        "#######                             #######\n"
        "###########################################\n"
        "-------------------------------------------"
    )