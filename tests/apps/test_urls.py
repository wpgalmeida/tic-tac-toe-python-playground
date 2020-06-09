from django.db import IntegrityError
from django.test import TestCase, Client

from tic_tac_toe_python_playground.apps.core.models import Player, Board, PlayerBoard, Game, Movements


class CrudTestPlayer(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_should_post_player(self):
        # test create
        player_to_be_created = {"name": "Player One", "birth": "2020-05-31", "gender": "M", "bot": False}

        content_type = "application/json"
        response = self.client.post("/api-players/", data=player_to_be_created, content_type=content_type)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Player.objects.count(), 1)

        update_object = Player.objects.first()

        self.assertEqual(update_object.name, "Player One")
        # self.assertEqual(update_object.birth, "2020-05-31")
        self.assertEqual(update_object.gender, "M")
        self.assertFalse(update_object.bot)

    def test_should_get_players(self):
        # test read
        sample_player = Player.objects.create(name="Bot", birth="2020-5-15", gender="O")
        response = self.client.get("/api-players/")

        self.assertEqual(response.status_code, 200)

        content_as_json = response.json()

        self.assertEqual(content_as_json["count"], 1)
        self.assertEqual(content_as_json["next"], None)
        self.assertEqual(content_as_json["previous"], None)
        self.assertEqual(content_as_json["results"][0]["name"], sample_player.name)
        self.assertEqual(content_as_json["results"][0]["gender"], sample_player.gender)
        self.assertFalse(content_as_json["results"][0]["bot"])

    def test_should_update_player(self):
        # test update
        sample_player = Player.objects.create(name="Player One", birth="2020-5-15", gender="M", bot=False)
        player_to_be_persisted = {"name": "Player One", "birth": "2020-05-31", "gender": "M", "bot": True}
        content_type = "application/json"

        response = self.client.patch(
            "/api-players/" + str(sample_player.id) + "/", data=player_to_be_persisted, content_type=content_type
        )

        updated_player = Player.objects.first()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Player.objects.count(), 1)
        self.assertEqual(updated_player.name, "Player One")
        # self.assertEqual(updated_player.birth, "2020-05-31")
        self.assertEqual(updated_player.gender, "M")
        self.assertTrue(updated_player.bot)

    def test_should_delete_player(self):
        # test delete
        sample_player = Player.objects.create(name="Player One", birth="2020-5-15", gender="M", bot=False)

        self.assertEqual(Player.objects.count(), 1)

        response = self.client.delete("/api-players/" + str(sample_player.id) + "/")

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Player.objects.count(), 0)


class CrudTestBoard(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_should_post_board(self):
        # test create board
        board_to_be_created = {"num_cols": 3, "num_rows": 3}
        content_type = "application/json"
        response = self.client.post("/api-boards/", data=board_to_be_created, content_type=content_type)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Board.objects.count(), 1)

        created_board: Board = Board.objects.first()

        self.assertEqual(created_board.num_rows, 3)
        self.assertEqual(created_board.num_cols, 3)

    def test_should_get_players(self):
        # test read board
        Board.objects.create(num_rows=3, num_cols=3)
        response = self.client.get("/api-boards/")

        self.assertEqual(response.status_code, 200)

        created_board: Board = Board.objects.first()

        self.assertEqual(Board.objects.count(), 1)
        self.assertEqual(created_board.num_cols, 3)
        self.assertEqual(created_board.num_rows, 3)

    def test_should_update_player(self):
        # test update board
        Board.objects.create(num_rows=3, num_cols=3)
        board_to_be_updated = {"num_cols": 4, "num_rows": 4}
        created_board: Board = Board.objects.first()
        content_type = "application/json"

        self.assertEqual(created_board.num_cols, 3)
        self.assertEqual(created_board.num_rows, 3)

        response = self.client.patch(
            "/api-board/" + str(created_board.id) + "/", data=board_to_be_updated, content_type=content_type
        )

        self.assertEqual(response.status_code, 200)

        update_board = Board.objects.first()

        self.assertEqual(Board.objects.count(), 1)
        self.assertEqual(update_board.num_cols, 4)
        self.assertEqual(update_board.num_rows, 4)

    def test_should_delete_player(self):
        # test delete pass
        Board.objects.create(num_rows=3, num_cols=3)
        created_board: Board = Board.objects.first()

        self.assertEqual(Board.objects.count(), 1)

        response = self.client.delete("/api-board/" + str(created_board.id) + "/")

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Board.objects.count(), 0)


class CrudTestPlayerBoard(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_should_post_player_board(self):
        # test create PlayerBoard
        content_type = "application/json"
        sample_player = Player.objects.create(name="Player One", birth="2020-5-15", gender="M", bot=False)
        sample_board = Board.objects.create(num_cols=3, num_rows=3)

        # sample_board = Board.objects.first()
        # sample_player = Player.objects.first()

        response_player = self.client.get("/api-players/")
        response_board = self.client.get("/api-boards/")

        p_json = response_player.json()
        b_json = response_board.json()

        player_board_to_be_created = {
            "player": p_json["results"][0]["id"],
            "board": b_json["results"][0]["id"],
            "symbol": "X",
        }

        response = self.client.post("/api-player-board/", data=player_board_to_be_created, content_type=content_type,)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(PlayerBoard.objects.count(), 1)

        created_player_board: PlayerBoard = PlayerBoard.objects.first()

        self.assertEqual(created_player_board.board, sample_board)
        self.assertEqual(created_player_board.player, sample_player)
        self.assertEqual(created_player_board.symbol, "X")

    def test_should_get_players(self):
        # test read Playerboard
        sample_player = Player.objects.create(name="Player One", birth="2020-5-15", gender="M", bot=False)
        sample_board = Board.objects.create(num_cols=3, num_rows=3)
        sample_player_board = PlayerBoard.objects.create(player=sample_player, board=sample_board, symbol="X")

        response = self.client.get("/api-player-board/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(PlayerBoard.objects.count(), 1)

        created_player_board: PlayerBoard = PlayerBoard.objects.first()

        self.assertEqual(created_player_board.board, sample_player_board.board)
        self.assertEqual(created_player_board.player, sample_player_board.player)
        self.assertEqual(created_player_board.symbol, sample_player_board.symbol)

    def test_should_update_player(self):
        # test update PlayerBoard
        sample_player = Player.objects.create(name="Player One", birth="2020-5-15", gender="M", bot=False)
        sample_board = Board.objects.create(num_cols=3, num_rows=3)
        sample_player_board: PlayerBoard = PlayerBoard.objects.create(
            player=sample_player, board=sample_board, symbol="X"
        )
        player_board_to_be_updated = {
            "player": str(sample_player_board.player.id),
            "board": str(sample_player_board.board.id),
            "symbol": "O",
        }
        content_type = "application/json"

        response = self.client.patch(
            "/api-player-board/" + str(sample_player_board.id) + "/",
            data=player_board_to_be_updated,
            content_type=content_type,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(PlayerBoard.objects.count(), 1)

        created_player_board: PlayerBoard = PlayerBoard.objects.first()

        self.assertEqual(created_player_board.board, sample_player_board.board)
        self.assertEqual(created_player_board.player, sample_player_board.player)
        self.assertEqual(created_player_board.symbol, "O")

    def test_should_delete_player(self):
        # test delete PlayerBoard
        sample_player = Player.objects.create(name="Player One", birth="2020-5-15", gender="M", bot=False)
        sample_board = Board.objects.create(num_cols=3, num_rows=3)
        sample_player_board: PlayerBoard = PlayerBoard.objects.create(
            player=sample_player, board=sample_board, symbol="X"
        )

        self.assertEqual(PlayerBoard.objects.count(), 1)

        response = self.client.delete("/api-player-board/" + str(sample_player_board.id) + "/")

        self.assertEqual(response.status_code, 204)
        self.assertEqual(PlayerBoard.objects.count(), 0)


class CrudTestGame(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.sample_board = Board.objects.create(num_rows=3, num_cols=3)
        self.content_type = "application/json"
        self.url_api_game = "/api-game/"

    def test_should_post_game(self):
        # test create Game
        board_id = self.sample_board.id
        game_to_be_created = {"board": str(board_id)}
        response = self.client.post(self.url_api_game, data=game_to_be_created, content_type=self.content_type)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Game.objects.count(), 1)

        created_game = Game.objects.first()

        self.assertEqual(created_game.board, self.sample_board)
        self.assertIsNone(created_game.winner)
        self.assertFalse(created_game.draw)

    def test_should_get_game(self):
        # test read Game
        Game.objects.create(board=self.sample_board)

        response = self.client.get(self.url_api_game)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Game.objects.count(), 1)

        created_game = Game.objects.first()

        self.assertEqual(created_game.board, self.sample_board)
        self.assertIsNone(created_game.winner)
        self.assertFalse(created_game.draw)

    def test_should_update_game(self):
        # test update Game
        sample_game = Game.objects.create(board=self.sample_board)
        game_to_be_updated = {"board": str(self.sample_board.id), "draw": True}
        response = self.client.patch(
            self.url_api_game + str(sample_game.id) + "/", data=game_to_be_updated, content_type=self.content_type
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Game.objects.count(), 1)

        created_game = Game.objects.first()

        self.assertEqual(created_game.board, self.sample_board)
        self.assertIsNone(created_game.winner)
        self.assertTrue(created_game.draw)

    def test_should_delete_game(self):
        # test delete Game
        sample_game = Game.objects.create(board=self.sample_board)

        self.assertEqual(Game.objects.count(), 1)

        response = self.client.delete(self.url_api_game + str(sample_game.id) + "/")

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Game.objects.count(), 0)


class CrudTestMovements(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.sample_player = Player.objects.create(name="Player One", birth="2020-5-15", gender="M", bot=False)
        self.sample_board = Board.objects.create(num_rows=3, num_cols=3)
        self.content_type = "application/json"
        self.url_api_movements = "/api-movement/"

    def test_should_post_movements(self):
        # test create Movements
        movements_to_be_created = {
            "player": str(self.sample_player.id),
            "board": str(self.sample_board.id),
            "position": 9,
        }
        response = self.client.post(
            self.url_api_movements, data=movements_to_be_created, content_type=self.content_type
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Movements.objects.count(), 1)

        created_movements: Movements = Movements.objects.first()

        self.assertEqual(created_movements.board, self.sample_board)
        self.assertEqual(created_movements.player, self.sample_player)
        self.assertEqual(created_movements.position, 9)

    def test_should_get_movements(self):
        # test read Movements
        Movements.objects.create(player=self.sample_player, board=self.sample_board, position=9)
        response = self.client.get(self.url_api_movements)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Movements.objects.count(), 1)

        created_movements: Movements = Movements.objects.first()

        self.assertEqual(created_movements.board, self.sample_board)
        self.assertEqual(created_movements.player, self.sample_player)
        self.assertEqual(created_movements.position, 9)

    def test_should_update_movements(self):
        # test update Movements
        sample_movements = Movements.objects.create(player=self.sample_player, board=self.sample_board, position=9)
        movements_to_be_updated = {
            "position": 7,
        }

        self.assertEqual(sample_movements.position, 9)

        response = self.client.patch(
            self.url_api_movements + str(sample_movements.id) + "/",
            data=movements_to_be_updated,
            content_type=self.content_type,
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(Movements.objects.count(), 1)

        created_movements: Movements = Movements.objects.first()

        self.assertEqual(created_movements.board, self.sample_board)
        self.assertEqual(created_movements.player, self.sample_player)
        self.assertEqual(created_movements.position, 7)

    def test_should_delete_movements(self):
        # test delete Movements
        sample_movements = Movements.objects.create(player=self.sample_player, board=self.sample_board, position=9)

        self.assertEqual(Movements.objects.count(), 1)

        response = self.client.delete(self.url_api_movements + str(sample_movements.id) + "/")

        self.assertEqual(response.status_code, 204)
        self.assertEqual(Movements.objects.count(), 0)


# General tests
class ApiTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.content_type = "application/json"
        self.url_api_movements = "/api-movement/"
        self.url_api_player = "/api-players/"
        self.sample_player_one = Player.objects.create(name="Player One", birth="2020-5-15", gender="M", bot=False)
        self.sample_player_two = Player.objects.create(name="Player Two", birth="2020-5-15", gender="M", bot=True)
        self.sample_board = Board.objects.create(num_rows=3, num_cols=3)
        self.sample_movement = Movements.objects.create(
            player=self.sample_player_one, board=self.sample_board, position=0
        )

    def test_should_raise_constraint_given_movement_in_same_position(self):
        movement_to_be_created = {
            "player": str(self.sample_player_one.id),
            "board": str(self.sample_board.id),
            "position": 0,
        }

        with self.assertRaisesMessage(
            IntegrityError, "UNIQUE constraint failed: core_movements.position, " "core_movements.board_id"
        ):
            response = self.client.post(
                self.url_api_movements, data=movement_to_be_created, content_type=self.content_type
            )

    def test_should_400_given_move_with_non_exist_player(self):
        movement_to_be_created = {
            "player": "xpto",
            "board": str(self.sample_board.id),
            "position": 0,
        }
        response = self.client.post(self.url_api_movements, data=movement_to_be_created, content_type=self.content_type)
        # bad request
        self.assertEqual(response.status_code, 400)

    def test_should_400_given_move_with_non_exist_board(self):
        movement_to_be_created = {
            "player": str(self.sample_player_one.id),
            "board": "xpto",
            "position": 0,
        }
        response = self.client.post(self.url_api_movements, data=movement_to_be_created, content_type=self.content_type)
        # bad request
        self.assertEqual(response.status_code, 400)

    def test_should_delete_player_that_is_playing(self):
        PlayerBoard.objects.create(player=self.sample_player_one, board=self.sample_board, symbol="X")
        qs = Player.objects.filter(id=self.sample_player_one.id)

        self.assertEqual(qs.count(), 1)

        response = self.client.delete(self.url_api_player + str(self.sample_player_one.id) + "/")
        qs = Player.objects.filter(id=self.sample_player_one.id)

        self.assertEqual(qs.count(), 0)
        self.assertEqual(response.status_code, 204)


class SimulationGame(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.content_type = "application/json"
        self.url_api_movements = "/api-movement/"
        self.url_api_player = "/api-players/"
        self.url_api_board = "/api-boards/"
        self.url_api_player_board = "/api-player-board/"
        self.url_api_game = "/api-game/"
        self.url_api_v1_movement = "/api/v1/movement/"

    def test_should_execute_all_process_of_game(self):
        # POST / api - players /

        player_one_to_be_created = {"name": "Player One", "birth": "2020-01-01", "gender": "M", "bot": False}
        response_p1 = self.client.post(
            self.url_api_player, data=player_one_to_be_created, content_type=self.content_type
        )
        player_one = response_p1.json()

        player_bot_to_be_created = {"name": "Bot", "birth": "2020-01-01", "gender": "M", "bot": True}
        response_p2 = self.client.post(
            self.url_api_player, data=player_bot_to_be_created, content_type=self.content_type
        )
        player_bot = response_p2.json()

        # POST / api - boards /
        board_two_be_created = {"num_cols": 3, "num_rows": 3}
        response_board = self.client.post(self.url_api_board, data=board_two_be_created, content_type=self.content_type)
        board = response_board.json()

        # POST / api - player - board /
        player_board_to_be_created = {"symbol": "X", "player": player_one["id"], "board": board["id"]}
        response_pb_one = self.client.post(
            self.url_api_player_board, data=player_board_to_be_created, content_type=self.content_type
        )

        player_board_to_be_created = {"symbol": "O", "player": player_bot["id"], "board": board["id"]}
        response_pb_bot = self.client.post(
            self.url_api_player_board, data=player_board_to_be_created, content_type=self.content_type
        )

        # POST / api - game /
        game_to_be_created = {"draw": False, "board": board["id"], "winner": None}
        reśponse_game = self.client.post(self.url_api_game, data=game_to_be_created, content_type=self.content_type)

        # POST /api-movement/
        movement_to_be_created = {"position": 0, "player": player_one["id"], "board": board["id"]}
        response_movement = self.client.post(
            self.url_api_v1_movement, data=movement_to_be_created, content_type=self.content_type
        )
        m_1 = response_movement.json()

        movement_to_be_created = {"position": 1, "player": player_bot["id"], "board": board["id"]}
        response_movement = self.client.post(
            self.url_api_movements, data=movement_to_be_created, content_type=self.content_type
        )
        m_2 = response_movement.json()

        self.assertEqual(m_2["player"], movement_to_be_created["player"])
        self.assertEqual(m_2["board"], movement_to_be_created["board"])
        self.assertEqual(m_2["position"], movement_to_be_created["position"])
