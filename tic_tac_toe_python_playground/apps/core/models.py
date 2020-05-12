import uuid

from django.db import models

# Create your models here.


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    bot = models.BooleanField(default=False)

    def __str__(self):
       return self.name


class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    num_cols = models.IntegerField()
    num_rows = models.IntegerField()


class PlayerBoard(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=1)


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)


class Movements(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    position = models.IntegerField()


class PlayerGame(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    winner = models.BooleanField(default=False)
    draw = models.BooleanField(default=False)
