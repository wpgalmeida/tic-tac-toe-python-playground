from django.test import TestCase

from tic_tac_toe_python_playground.apps.core.models import Player, Board


class Test(TestCase):
    def test_should_create_player(self):
        Player.objects.create(name="Trutão", symbol="X")
        expected_value = 1
        self.assertEquals(Player.objects.count(), expected_value)

    def test_should_create_board(self):
        Board.objects.create(num_cols=3, num_rows=3)
        expected_value = 1
        self.assertEquals(Board.objects.count(), expected_value)

    def test_should_create_game(self):
        self.fail()

    def test_should_create_movements(self):
        self.fail()


