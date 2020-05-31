from django.test import TestCase, Client

from tic_tac_toe_python_playground.apps.core.models import Player, Board


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
