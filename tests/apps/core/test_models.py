from django.test import TestCase

from tic_tac_toe_python_playground.apps.core.models import Player, Board, Game, PlayerBoard, PlayerGame, Movements


class Test(TestCase):
    def test_should_create_two_players(self):
        name_one = 'Player one'
        name_two = 'Player two'
        Player.objects.create(name=name_one)
        Player.objects.create(name=name_two, bot=True)
        expected_count_value = 2
        returned_value = Player.objects.all()

        self.assertEquals(Player.objects.count(), expected_count_value)
        self.assertEquals(str(returned_value[0]), name_one)
        self.assertEquals(str(returned_value[1]), name_two)

    def test_should_create_board_3_3(self):
        Board.objects.create(num_cols=3, num_rows=3)
        expected_value = 1

        self.assertEquals(Board.objects.count(), expected_value)
        self.assertEquals(Board.objects.all().first().num_cols, 3)
        self.assertEquals(Board.objects.all().first().num_rows, 3)

    def test_should_create_player_board(self):
        player = Player.objects.create(name='player one')
        board = Board.objects.create(num_cols=3, num_rows=3)
        PlayerBoard.objects.create(player=player, board=board, symbol='X')
        expected_count_value = 1

        self.assertEquals(PlayerBoard.objects.count(), expected_count_value)

    def test_should_create_two_player_board_with_the_same_board(self):
        player_one = Player.objects.create(name='player one')
        player_two = Player.objects.create(name='player two')
        board = Board.objects.create(num_cols=3, num_rows=3)
        PlayerBoard.objects.create(player=player_one, board=board, symbol='X')
        PlayerBoard.objects.create(player=player_two, board=board, symbol='O')
        expected_count_value = 2

        self.assertEquals(PlayerBoard.objects.count(), expected_count_value)

    def test_should_non_create_two_player_board_with_the_same_board_and_same_player(self):
        player_one = Player.objects.create(name='player one')
        board = Board.objects.create(num_cols=3, num_rows=3)
        PlayerBoard.objects.create(player=player_one, board=board, symbol='X')
        PlayerBoard.objects.create(player=player_one, board=board, symbol='X')
        expected_count_value = 1

        self.assertEquals(PlayerBoard.objects.count(), expected_count_value)
        self.fail()

    def test_should_create_game(self):
        board = Board.objects.create(num_rows=3, num_cols=3)
        Game.objects.create(board=board)
        expected_count_value = 1

        self.assertEquals(Game.objects.count(), expected_count_value)

    def test_should_create_player_game(self):
        player = Player.objects.create(name="player one")
        board = Board.objects.create(num_cols=3, num_rows=3)
        game = Game.objects.create(board=board)
        PlayerGame.objects.create(player=player, game=game)
        expected_count_value = 1

        self.assertEquals(PlayerGame.objects.count(), expected_count_value)

    def test_should_create_two_player_game_in_the_same_board(self):
        player_one = Player.objects.create(name="player one")
        player_two = Player.objects.create(name="player two")
        board = Board.objects.create(num_cols=3, num_rows=3)
        game = Game.objects.create(board=board)
        PlayerGame.objects.create(player=player_one, game=game)
        PlayerGame.objects.create(player=player_two, game=game)
        expected_count_value = 2

        self.assertEquals(PlayerGame.objects.count(), expected_count_value)

    def test_should_non_create_two_times_the_same_player_in_the_same_player_game(self):
        player_one = Player.objects.create(name="player one")
        board = Board.objects.create(num_cols=3, num_rows=3)
        game = Game.objects.create(board=board)
        PlayerGame.objects.create(player=player_one, game=game)
        PlayerGame.objects.create(player=player_one, game=game)
        expected_count_value = 1

        self.assertEquals(PlayerGame.objects.count(), expected_count_value)
        self.fail()

    def test_should_create_movements(self):
        player = Player.objects.create(name="player one")
        board = Board.objects.create(num_rows=3, num_cols=3)
        Movements.objects.create(player=player, board=board, position=0)
        expected_count_value = 1

        self.assertEquals(Movements.objects.count(), expected_count_value)




