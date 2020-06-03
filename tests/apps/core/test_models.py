from time import strptime

from django.db import IntegrityError
from django.test import TestCase

from tic_tac_toe_python_playground.apps.core.models import Player, Board, Game, PlayerBoard, Movements


class Test(TestCase):
    def test_should_create_real_player(self):
        name_of_player = "Player one"
        birth_of_player = "1989-1-25"
        gender_of_player = "M"
        expected_count_value = 1
        Player.objects.create(name=name_of_player, birth=birth_of_player, gender=gender_of_player)
        created_player = Player.objects.all().first()

        self.assertEquals(Player.objects.all().count(), expected_count_value)
        self.assertEquals(created_player.name, name_of_player)
        #        self.assertEquals(created_player.birth, birth_of_player)
        self.assertEquals(created_player.gender, gender_of_player)
        self.assertFalse(created_player.bot)

    def test_should_create_bot_player(self):
        name_of_player = "Bot"
        birth_of_player = "2020-05-15"
        gender_of_player = "O"
        expected_count_value = 1
        Player.objects.create(name=name_of_player, birth=birth_of_player, gender=gender_of_player, bot=True)
        created_player = Player.objects.all().first()

        self.assertEquals(Player.objects.all().count(), expected_count_value)
        self.assertEquals(created_player.name, name_of_player)
        #        self.assertEquals(created_player.birth, birth_of_player)
        self.assertEquals(created_player.gender, gender_of_player)
        self.assertTrue(created_player.bot)

    def test_should_raise_given_player_without_name(self):
        birth_of_player = "1989-1-25"
        gender_of_player = "M"

        with self.assertRaisesMessage(IntegrityError, "NOT NULL constraint failed: core_player.name"):
            Player.objects.create(birth=birth_of_player, gender=gender_of_player, name=None)

    def test_should_raise_given_player_without_birth(self):
        name_of_player = "Player one"
        gender_of_player = "M"

        with self.assertRaisesMessage(IntegrityError, "NOT NULL constraint failed: core_player.birth"):
            Player.objects.create(name=name_of_player, gender=gender_of_player, birth=None)

    def test_should_raise_given_player_without_gender(self):
        name_of_player = "Player one"
        birth_of_player = "2020-05-15"

        with self.assertRaisesMessage(IntegrityError, "NOT NULL constraint failed: core_player.gender"):
            Player.objects.create(name=name_of_player, birth=birth_of_player, gender=None)

    def test_should_create_board_3_3(self):
        Board.objects.create(num_cols=3, num_rows=3)
        expected_count_value = 1

        self.assertEquals(Board.objects.count(), expected_count_value)
        self.assertEquals(Board.objects.all().first().num_cols, 3)
        self.assertEquals(Board.objects.all().first().num_rows, 3)

    def test_should_raise_given_create_board_without_number_of_cols(self):
        with self.assertRaisesMessage(IntegrityError, "NOT NULL constraint failed: core_board.num_cols"):
            Board.objects.create(num_rows=3)

    def test_should_raise_given_create_board_without_number_of_rows(self):
        with self.assertRaisesMessage(IntegrityError, "NOT NULL constraint failed: core_board.num_rows"):
            Board.objects.create(num_cols=3)

    def test_should_create_player_board(self):
        name_of_player = "Player one"
        birth_of_player = "1989-1-25"
        gender_of_player = "M"
        player = Player.objects.create(name=name_of_player, birth=birth_of_player, gender=gender_of_player)
        board = Board.objects.create(num_cols=3, num_rows=3)
        PlayerBoard.objects.create(player=player, board=board, symbol="X")
        expected_count_value = 1

        self.assertEquals(PlayerBoard.objects.count(), expected_count_value)

    def test_should_raise_given_create_player_board_without_symbol(self):
        name_of_player = "Player one"
        birth_of_player = "1989-1-25"
        gender_of_player = "M"
        player = Player.objects.create(name=name_of_player, birth=birth_of_player, gender=gender_of_player)
        board = Board.objects.create(num_cols=3, num_rows=3)

        with self.assertRaisesMessage(IntegrityError, "NOT NULL constraint failed: core_playerboard.symbol"):
            PlayerBoard.objects.create(player=player, board=board)

    def test_should_create_two_player_board_with_the_same_board(self):
        name_of_player_one = "Player one"
        birth_of_player_one = "1989-1-25"
        gender_of_player_one = "M"
        name_of_player_two = "Player two"
        birth_of_player_two = "2000-1-1"
        gender_of_player_two = "F"
        p1 = Player.objects.create(name=name_of_player_one, birth=birth_of_player_one, gender=gender_of_player_one)
        p2 = Player.objects.create(name=name_of_player_two, birth=birth_of_player_two, gender=gender_of_player_two)
        board = Board.objects.create(num_cols=3, num_rows=3)
        PlayerBoard.objects.create(player=p1, board=board, symbol="X")
        PlayerBoard.objects.create(player=p2, board=board, symbol="O")
        expected_count_value = 2

        self.assertEquals(PlayerBoard.objects.count(), expected_count_value)

    def test_should_raise_constraint_given_create_two_player_board_with_the_same_board_and_same_player(self):
        name_of_player_one = "Player one"
        birth_of_player_one = "1989-1-25"
        gender_of_player_one = "M"
        p1 = Player.objects.create(name=name_of_player_one, birth=birth_of_player_one, gender=gender_of_player_one)
        board = Board.objects.create(num_cols=3, num_rows=3)
        PlayerBoard.objects.create(player=p1, board=board, symbol="X")

        with self.assertRaisesMessage(
            IntegrityError, "UNIQUE constraint failed: core_playerboard.player_id, " "core_playerboard.board_id"
        ):
            PlayerBoard.objects.create(player=p1, board=board, symbol="O")

    def test_should_create_game(self):
        board = Board.objects.create(num_rows=3, num_cols=3)
        Game.objects.create(board=board)
        expected_count_value = 1
        created_game = Game.objects.all().first()

        self.assertEquals(Game.objects.count(), expected_count_value)
        self.assertFalse(created_game.draw)
        self.assertIsNone(created_game.winner)

    def test_should_create_draw_game(self):
        board = Board.objects.create(num_rows=3, num_cols=3)
        Game.objects.create(board=board, draw=True)
        expected_count_value = 1
        created_game = Game.objects.all().first()

        self.assertEquals(Game.objects.count(), expected_count_value)
        self.assertTrue(created_game.draw)
        self.assertIsNone(created_game.winner)

    def test_should_create_winner_game(self):
        board = Board.objects.create(num_rows=3, num_cols=3)
        p1 = Player.objects.create(name="Bot", birth="2020-5-15", gender="O")
        Game.objects.create(board=board, winner=p1)
        expected_count_value = 1
        created_game = Game.objects.all().first()

        self.assertEquals(Game.objects.count(), expected_count_value)
        self.assertFalse(created_game.draw)
        self.assertEquals(created_game.winner, p1)

    def test_should_create_movements(self):
        name_of_player_one = "Player one"
        birth_of_player_one = "1989-1-25"
        gender_of_player_one = "M"
        p1 = Player.objects.create(name=name_of_player_one, birth=birth_of_player_one, gender=gender_of_player_one)
        board = Board.objects.create(num_rows=3, num_cols=3)
        Movements.objects.create(player=p1, board=board, position=0)
        created_mov = Movements.objects.all().first()
        expected_count_value = 1

        self.assertEquals(Movements.objects.count(), expected_count_value)
        self.assertEquals(created_mov.position, 0)

    def test_should_raise_given_create_movements_without_position(self):
        name_of_player_one = "Player one"
        birth_of_player_one = "1989-1-25"
        gender_of_player_one = "M"
        p1 = Player.objects.create(name=name_of_player_one, birth=birth_of_player_one, gender=gender_of_player_one)
        board = Board.objects.create(num_rows=3, num_cols=3)

        with self.assertRaisesMessage(IntegrityError, "NOT NULL constraint failed: core_movements.position"):
            Movements.objects.create(player=p1, board=board)

    def test_should_raise_given_create_two_movements_in_the_same_board_and_position(self):
        name_of_player_one = "Player one"
        birth_of_player_one = "1989-1-25"
        gender_of_player_one = "M"
        p1 = Player.objects.create(name=name_of_player_one, birth=birth_of_player_one, gender=gender_of_player_one)
        board = Board.objects.create(num_rows=3, num_cols=3)
        Movements.objects.create(player=p1, board=board, position=0)

        with self.assertRaisesMessage(
            IntegrityError, "UNIQUE constraint failed: core_movements.position, " "core_movements.board_id"
        ):
            Movements.objects.create(player=p1, board=board, position=0)

    def test_should_create_two_movements_with_the_same_player(self):
        name_of_player_one = "Player one"
        birth_of_player_one = "1989-1-25"
        gender_of_player_one = "M"
        p1 = Player.objects.create(name=name_of_player_one, birth=birth_of_player_one, gender=gender_of_player_one)
        board = Board.objects.create(num_rows=3, num_cols=3)
        Movements.objects.create(player=p1, board=board, position=0)
        Movements.objects.create(player=p1, board=board, position=1)
        expected_count_value = 2

        self.assertEquals(Movements.objects.all().count(), expected_count_value)

    def test_should_create_two_movements_with_diferents_players(self):
        name_of_player_one = "Player one"
        birth_of_player_one = "1989-1-25"
        gender_of_player_one = "M"
        p1 = Player.objects.create(name=name_of_player_one, birth=birth_of_player_one, gender=gender_of_player_one)
        name_of_player_two = "Bot"
        birth_of_player_two = "2020-5-16"
        gender_of_player_two = "O"
        p2 = Player.objects.create(
            name=name_of_player_two, birth=birth_of_player_two, gender=gender_of_player_two, bot=True
        )
        board = Board.objects.create(num_rows=3, num_cols=3)
        Movements.objects.create(player=p1, board=board, position=0)
        Movements.objects.create(player=p2, board=board, position=1)
        expected_count_value = 2

        self.assertEquals(Movements.objects.all().count(), expected_count_value)

    def test_should_return_all_movements_with_symbol_X_given_one_finished_game_with_5_movements(self):
        # player
        name_of_player_one = "Player one"
        birth_of_player_one = "1989-1-25"
        gender_of_player_one = "M"
        p1_symbol = "X"
        p1 = Player.objects.create(name=name_of_player_one, birth=birth_of_player_one, gender=gender_of_player_one)
        name_of_player_two = "Bot"
        birth_of_player_two = "2020-1-5"
        gender_of_player_two = "O"
        p2_symbol = "O"
        p2 = Player.objects.create(name=name_of_player_two, birth=birth_of_player_two, gender=gender_of_player_two)
        # board
        board = Board.objects.create(num_rows=3, num_cols=3)
        # playerboard
        PlayerBoard.objects.create(player=p1, board=board, symbol=p1_symbol)
        PlayerBoard.objects.create(player=p2, board=board, symbol=p2_symbol)
        # game
        game = Game.objects.create(board=board)
        # movement one
        movement = Movements.objects.create(player=p1, board=board, position=0)
        movement = Movements.objects.create(player=p2, board=board, position=3)
        movement = Movements.objects.create(player=p1, board=board, position=1)
        movement = Movements.objects.create(player=p2, board=board, position=4)
        movement = Movements.objects.create(player=p1, board=board, position=2)
        # update game
        Game.objects.filter(id=game.id).update(winner=p1)

        """
        pb = PlayerBoard.objects.filter(symbol='X').get()
        mv = Movements.objects.filter(player=pb.player)
        """
        mv = Movements.objects.filter(player__playerboard__symbol="X", board__game__draw__exact=True)
        entry_list = list(mv)
        for pos in mv:
            print(pos.position)
            print(pos.player)
            print(pos.board)
