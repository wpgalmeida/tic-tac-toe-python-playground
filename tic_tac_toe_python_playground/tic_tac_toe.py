class BoardDoesNotHaveTheMinimalConfiguration(Exception):
    pass


class BoardDoesNotHaveTheMaximumConfiguration(Exception):
    pass


class CellAlreadyWasPlayedPlayAgain(Exception):
    pass


class CellIsNotValid(Exception):
    pass


def _print_header():
    print(
        "###########################################\n"
        "#######                             #######\n"
        "####### BEM VINDO AO JOGO DA VELHA! #######\n"
        "#######                             #######\n"
        "###########################################\n"
        "-------------------------------------------"
    )


def _print_welcome_mess():
    print("Bem vindo ao jogo, vamos começar!")


def _choice_size_board():
    return int(input("Quantas linhas desesja em seu tabuleiro:"))


def define_game_players():
    options_game_players = "[1] - Humano Vs PC\n"\
                           "[2] - Humano Vs Humano\n"\
                           "[3] - PC Vs PC\n"\
                           "Escolha uma opção:"

    option = int(input(options_game_players))

    if option == 1:
        p1 = set_type_player_one_is_bot(False)
        p2 = set_type_player_two_is_bot(True)
    elif option == 2:
        p1 = set_type_player_one_is_bot(False)
        p2 = set_type_player_two_is_bot(False)
    elif option == 3:
        p1 = set_type_player_one_is_bot(True)
        p2 = set_type_player_two_is_bot(True)

    return(p1, p2)


def _print_board(board):
    size = len(board)
    aux_lin = 0

    for row in board:
        aux_lin +=1
        aux_col = 0
        mask_board_to_print = ""
        line = ""

        for cell in row:
            aux_col +=1
            mask_board_to_print = mask_board_to_print + "  " + format(cell, '02')

            if aux_col < size:
                mask_board_to_print = mask_board_to_print + "  |"
                line = line + "_________"

        print(mask_board_to_print)
        if aux_lin < size:
            print(line)


def to_play_tic_tac_toe():
    _print_header()
    p1, p2 = define_game_players()

    size_board = _choice_size_board()
    board = create_board(size_board)

    _print_board(board)
    _print_welcome_mess()

#    make_move(board, )


def create_board(size=3):
    board = []
    count = 0

    for row in range(0, size):
        board.append([])
        for col in range(0, size):
            board[row].append(count)
            count += 1

    return board

def make_move(actual_board, symbol, positon):
    pass


def check_win(board):
    pass


def check_end_game(actual_board):
    pass


def set_type_player_one_is_bot(bot: bool):
    player_one = {
        'Simbol': 'X',
        'Bot': bot,
        'MyTurn': None
    }
    return (player_one)


def set_type_player_two_is_bot(bot: bool):
    player_two = {
        'Simbol': 'O',
        'Bot': bot,
        'MyTurn': None
    }
    return (player_two)


if __name__ == '__main__':
    to_play_tic_tac_toe()
