from datetime import datetime

from django.db import IntegrityError
from django.test import TestCase

from tic_tac_toe_python_playground.apps.core.models import Player, Board, PlayerBoard


class Test(TestCase):
    def setUp(self) -> None:
        self.name = "Augusto Carrara"
        str_birth = "2020-01-01"
        self.birth = datetime.strptime(str_birth, "%Y-%m-%d").date()
        self.gender = "M"

        self.name_p2 = "O Turco"
        self.birth_p2 = datetime.strptime(str_birth, "%Y-%m-%d").date()
        self.gender_p2 = "o"

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
            name=self.name_p2, birth=self.birth_p2, gender=self.gender_p2, bot=True
        )
        created_player = Player.objects.first()

        self.assertEqual(Player.objects.all().count(), expected_count_value)
        self.assertEqual(created_player.name, self.name_p2)
        self.assertEqual(created_player.birth, self.birth_p2)
        self.assertEqual(created_player.gender, self.gender_p2)
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

    # tests for player_board
    def test_should_create_player_board(self):
        expected_count_value = 1
        player = Player.objects.create(
            name=self.name, birth=self.birth, gender=self.gender
        )
        board = Board.objects.create(num_rows=3)
        PlayerBoard.objects.create(player=player, board=board, symbol="X")

        created_player_board = PlayerBoard.objects.first()

        self.assertEqual(PlayerBoard.objects.all().count(), expected_count_value)
        self.assertEqual(created_player_board.symbol, "X")

    def test_should_raise_not_null_constraint_given_create_player_board_without_symbol(
        self,
    ):
        player = Player.objects.create(
            name=self.name, birth=self.birth, gender=self.gender
        )
        board = Board.objects.create(num_rows=3)

        with self.assertRaisesMessage(
            IntegrityError, "NOT NULL constraint failed: core_playerboard.symbol"
        ):
            PlayerBoard.objects.create(player=player, board=board)

    def test_should_create_two_differents_players_and_same_board(self,):
        expected_count_value = 2
        player_one = Player.objects.create(
            name=self.name, birth=self.birth, gender=self.gender
        )
        player_two = Player.objects.create(
            name=self.name_p2, birth=self.birth_p2, gender=self.gender_p2, bot=True
        )
        board = Board.objects.create(num_rows=3)
        PlayerBoard.objects.create(player=player_one, board=board, symbol="X")
        PlayerBoard.objects.create(player=player_two, board=board, symbol="O")

        player_board = PlayerBoard.objects.all()

        self.assertEqual(PlayerBoard.objects.all().count(), expected_count_value)

        self.assertEqual(player_board[0].player.name, self.name)
        self.assertEqual(player_board[0].player.birth, self.birth)
        self.assertEqual(player_board[0].player.gender, self.gender)
        self.assertFalse(player_board[0].player.bot)
        self.assertEqual(player_board[0].symbol, "X")

        self.assertEqual(player_board[1].player.name, self.name_p2)
        self.assertEqual(player_board[1].player.birth, self.birth_p2)
        self.assertEqual(player_board[1].player.gender, self.gender_p2)
        self.assertTrue(player_board[1].player.bot)
        self.assertEqual(player_board[1].symbol, "O")

        self.assertEqual(player_board[0].board, board)
        self.assertEqual(player_board[1].board, board)

    def test_should_create_two_player_board_with_the_same_player_and_differents_boards(self,):
        expected_count_value = 2
        player_one = Player.objects.create(
            name=self.name, birth=self.birth, gender=self.gender
        )
        board_one = Board.objects.create(num_rows=3)
        board_two = Board.objects.create(num_rows=4)
        PlayerBoard.objects.create(player=player_one, board=board_one, symbol="X")
        PlayerBoard.objects.create(player=player_one, board=board_two, symbol="X")

        player_board = PlayerBoard.objects.all()

        self.assertEqual(PlayerBoard.objects.all().count(), expected_count_value)

    def test_should_raise_unique_constraint_given_create_two_times_the_same_player_in_a_player_board(
        self,
    ):
        player = Player.objects.create(
            name=self.name, birth=self.birth, gender=self.gender
        )
        board = Board.objects.create(num_rows=3)
        PlayerBoard.objects.create(player=player, board=board, symbol="X")

        with self.assertRaisesMessage(
            IntegrityError,
            "UNIQUE constraint failed: core_playerboard.player_id, core_playerboard.board_id",
        ):
            PlayerBoard.objects.create(player=player, board=board, symbol="O")

    def test_should_raise_given_create_player_board_with_the_same_symbol(self):
        player_one = Player.objects.create(
            name=self.name, birth=self.birth, gender=self.gender
        )
        player_two = Player.objects.create(
            name=self.name_p2, birth=self.birth_p2, gender=self.gender_p2, bot=True
        )
        board = Board.objects.create(num_rows=3)
        PlayerBoard.objects.create(player=player_one, board=board, symbol="X")

        with self.assertRaisesMessage(
            ValueError, "Escolha outro simbolo"
        ):
            PlayerBoard.objects.create(player=player_two, board=board, symbol="X")



