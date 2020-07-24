from datetime import datetime

from django.db import IntegrityError
from django.test import TestCase

from tic_tac_toe_python_playground.apps.core.models import Player, Board


class Test(TestCase):
    def setUp(self) -> None:
        self.name = "Augusto Carrara"
        str_birth = "2020-01-01"
        self.birth = datetime.strptime(str_birth, "%Y-%m-%d").date()
        self.gender = "M"

    # Tests for player
    def test_should_create_player(self):
        expected_count_value = 1

        Player.objects.create(name=self.name, birth=self.birth, gender=self.gender)
        created_player = Player.objects.first()

        self.assertEqual(Player.objects.all().count(), expected_count_value)
        self.assertEqual(created_player.name, self.name)
        self.assertEqual(created_player.birth, self.birth)
        self.assertEqual(created_player.gender, self.gender)
        self.assertFalse(created_player.bot)

    def test_should_create_player_bot(self):
        expected_count_value = 1

        Player.objects.create(
            name=self.name, birth=self.birth, gender=self.gender, bot=True
        )
        created_player = Player.objects.first()

        self.assertEqual(Player.objects.all().count(), expected_count_value)
        self.assertEqual(created_player.name, self.name)
        self.assertEqual(created_player.birth, self.birth)
        self.assertEqual(created_player.gender, self.gender)
        self.assertTrue(created_player.bot)

    def test_should_raise_given_player_without_name(self):
        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_player.name"
        ):
            Player.objects.create(name=None, birth=self.birth, gender=self.gender)

    def test_should_raise_given_player_without_gender(self):
        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_player.gender"
        ):
            Player.objects.create(name=self.name, birth=self.birth, gender=None)

    def test_should_raise_given_player_without_birth(self):
        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_player.birth"
        ):
            Player.objects.create(name=self.name, gender=self.gender)

    # Test for board
    def test_should_raise_given_board_with_number_rows_less_than_3(self):
        with self.assertRaisesMessage(
            ValueError, "Numero de linhas deve ser entre 3 e 6"
        ):
            Board.objects.create(num_rows=1)

    def test_should_raise_given_board_with_number_rows_greather_than_6(self):
        with self.assertRaisesMessage(
            ValueError, "Numero de linhas deve ser entre 3 e 6"
        ):
            Board.objects.create(num_rows=7)

    def test_should_create_board_with_3_rows(self):
        expected_count_value = 1

        Board.objects.create(num_rows=3)

        created_board: Board = Board.objects.first()

        self.assertEqual(Board.objects.all().count(), expected_count_value)
        self.assertEqual(created_board.num_rows, 3)

    def test_should_create_board_with_4_rows(self):
        expected_count_value = 1

        Board.objects.create(num_rows=4)

        created_board: Board = Board.objects.first()

        self.assertEqual(Board.objects.all().count(), expected_count_value)
        self.assertEqual(created_board.num_rows, 4)

    def test_should_create_board_with_5_rows(self):
        expected_count_value = 1

        Board.objects.create(num_rows=5)

        created_board: Board = Board.objects.first()

        self.assertEqual(Board.objects.all().count(), expected_count_value)
        self.assertEqual(created_board.num_rows, 5)

    def test_should_create_board_with_6_rows(self):
        expected_count_value = 1

        Board.objects.create(num_rows=6)

        created_board: Board = Board.objects.first()

        self.assertEqual(Board.objects.all().count(), expected_count_value)
        self.assertEqual(created_board.num_rows, 6)
