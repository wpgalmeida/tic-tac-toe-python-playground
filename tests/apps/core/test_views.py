from django.test import TestCase, Client


# GET POST PATCH/PUT DELETE

# 2XX - SUCCESS
# 3XX - REDIRECT
# 4XX - CONTRACT PROBLEM
#  - 400: you are missing something in order to do what I must do
#  - 405: this method is not allowed to execute this action
# 5XX - SERVER ERROR
from tic_tac_toe_python_playground.apps.core.models import Board, Game


class Test(TestCase):
    def test_should_call_my_first_api(self):
        client = Client()

        response = client.get("/api/sample/hello-world")

        content_as_str = response.content.decode()
        expected_result = "Hello, World!"

        self.assertEqual(content_as_str, expected_result)
        self.assertEqual(response.status_code, 200)

    def test_should_call_example_api_and_receive_405_given_the_method_is_not_allowed(self):
        client = Client()

        response = client.patch("/api/sample/hello-world")

        self.assertEqual(response.status_code, 405)

    def test_should_return_previous_created_games(self):
        client = Client()

        created_board = Board.objects.create(num_rows=3, num_cols=3)
        Game.objects.create(board=created_board)

        response = client.get("/api/sample/test-game")

        self.assertEqual(response.status_code, 200)

        content_as_json = response.json()
        list_of_games = content_as_json["games"]

        self.assertEqual(len(list_of_games), 1)
        self.assertEqual(list_of_games[0]["board_id"], str(created_board.id))
