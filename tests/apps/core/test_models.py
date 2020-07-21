from datetime import datetime

from django.test import TestCase

from tic_tac_toe_python_playground.apps.core.models import Player


class Test(TestCase):
    def test_should_create_player(self):
        name = "Augusto Carrara"
        birth = "2020-01-01"
        converted_birth = datetime.strptime(birth, "%Y-%m-%d").date()
        gender = "M"
        bot = False
        expected_count_value = 1

        Player.objects.create(name=name, birth=birth, gender=gender, bot=bot)
        created_player: Player = Player.objects.first()

        self.assertEqual(Player.objects.all().count(), expected_count_value)
        self.assertEqual(created_player.name, name)
        self.assertEqual(created_player.birth, converted_birth)
        self.assertEqual(created_player.gender, gender)
        self.assertEqual(created_player.bot, bot)
