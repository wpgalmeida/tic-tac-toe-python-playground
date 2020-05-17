from django.test import TestCase, Client

from tic_tac_toe_python_playground.apps.core.models import Player


class Test(TestCase):
    def test_should_return_all_players(self):
        client = Client()

        sample_player = Player.objects.create(name="Bot", birth="2020-5-15", gender="O")

        response = client.get("/drf-api/players/")

        self.assertEqual(response.status_code, 200)

        content_as_json = response.json()
        self.assertEqual(content_as_json["count"], 1)
        self.assertEqual(content_as_json["next"], None)
        self.assertEqual(content_as_json["previous"], None)
        self.assertEqual(content_as_json["results"][0]["name"], sample_player.name)
