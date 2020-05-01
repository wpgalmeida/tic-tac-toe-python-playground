from unittest import TestCase

from tic_tac_toe_python_playground.game_configurations import set_type_player_one_is_bot, set_type_player_two_is_bot


class Test(TestCase):
    def test_should_set_player_one(self):
        expected_player_one = {
            'Simbol': 'X',
            'Bot': False,
            'MyTurn': True
        }
        player_one = set_type_player_one_is_bot(False)
        self.assertEquals(expected_player_one, player_one)

    def test_should_set_player_two(self):
        expected_player_two = {
            'Simbol': 'O',
            'Bot': True,
            'MyTurn': None
        }
        player_two = set_type_player_two_is_bot(True)
        self.assertEquals(expected_player_two, player_two)
