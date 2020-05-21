from django.test import TestCase, Client

from tic_tac_toe_python_playground.apps.core.models import Board, Game


class SimpleTest(TestCase):
    def test_should_call_hello_world(self):
        client = Client()

        response = client.get("/hello-world/")

        content_as_str = response.content.decode()
        expected_result = 'Hello, World!'

        self.assertEqual(response.status_code, 200)
        self.assertEqual(content_as_str, expected_result)

    def test_should_call_hello_world_and_receive_405_given_the_method_is_not_allowed(self):
        client = Client()

        response = client.patch("/hello-world/")

        self.assertEqual(response.status_code, 405)

    def test_should_call_tic_tac_toe(self):
        client = Client()

        created_board = Board.objects.create(num_rows=3, num_cols=3)
        Game.objects.create(board=created_board)

        response = client.get("/tic-tac-toe/")

        content_as_json = response.json()
        list_of_games = content_as_json["games"]

        self.assertEquals(response.status_code, 200)
        self.assertEqual(len(list_of_games), 1)
        self.assertEqual(list_of_games[0]["board_id"], str(created_board.id))

    def test_should_call_tic_tac_toe_and_receive_405_given_the_method_is_not_allowed(self):
        client = Client()

        response = client.patch("/tic-tac-toe/")

        self.assertEqual(response.status_code, 405)
