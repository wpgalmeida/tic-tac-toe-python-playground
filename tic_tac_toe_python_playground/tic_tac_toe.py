from tic_tac_toe_python_playground.dealer import choice_move
from tic_tac_toe_python_playground.game_builder import create_board, BoardDoesNotHaveTheMinimalConfiguration, \
    BoardDoesNotHaveTheMaximumConfiguration
from tic_tac_toe_python_playground.game_configurations import define_game_players, choice_size_board
from tic_tac_toe_python_playground.jugde import check_end_game
from tic_tac_toe_python_playground.printer import print_welcome_mess, print_board, print_movement_count, \
    print_header


def to_play_tic_tac_toe():
    end_game = False
    count_move = 0
    board = None

    print_header()
    player_one, player_two = define_game_players()

    while type(board) is not type([]):
        size_board = choice_size_board()

        try:
            board = create_board(size_board)
            print_board(board)
            print_welcome_mess()
        except BoardDoesNotHaveTheMinimalConfiguration:
            print('O tabuleiro precisa ter no minimo 3 linhas')
        except BoardDoesNotHaveTheMaximumConfiguration:
            print('O tabuleiro não poder ter mais que 10 linhas')

    while not end_game:
        if player_one['MyTurn']:
            board = choice_move(board, player_one, player_two)
            count_move += 1
            print_movement_count(count_move)
            print_board(board)
            end_game = check_end_game(board)

        if not end_game and player_two['MyTurn']:
            board = choice_move(board, player_two, player_one)
            count_move += 1
            print_movement_count(count_move)
            print_board(board)
            end_game = check_end_game(board)


if __name__ == '__main__':
    to_play_tic_tac_toe()
