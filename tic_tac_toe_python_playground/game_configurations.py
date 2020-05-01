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


def choice_size_board():
    size = input("Quantas linhas deseja em seu tabuleiro:")
    return int(size)


def set_type_player_one_is_bot(bot: bool):
    player_one = {
        'Simbol': 'X',
        'Bot': bot,
        'MyTurn': True
    }
    return (player_one)


def set_type_player_two_is_bot(bot: bool):
    player_two = {
        'Simbol': 'O',
        'Bot': bot,
        'MyTurn': None
    }
    return (player_two)