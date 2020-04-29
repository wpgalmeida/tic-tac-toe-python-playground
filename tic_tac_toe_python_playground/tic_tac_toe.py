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


def _choice_size_board():
    return int(input("Quantas linhas desesja em seu tabuleiro:"))


def _choice_game_players():
    options_game_players = "[1] - Humano Vs PC\n"\
                           "[2] - Humano Vs Humano\n"\
                           "[3] - PC Vs PC\n"\
                           "Escolha uma opção:"

    return input(options_game_players)


def _print_board(board):
    for row in board:
            print(row)


def to_play_tic_tac_toe():
    _print_header()
    _choice_game_players()

    size_board = _choice_size_board()
    board = create_board(size_board)

    _print_board(board)

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

if __name__ == '__main__':
    to_play_tic_tac_toe()
