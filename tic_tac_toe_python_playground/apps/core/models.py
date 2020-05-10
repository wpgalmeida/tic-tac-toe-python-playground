import uuid

from django.db import models

# Create your models here.


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=1)
    bot = models.BooleanField(default=False)
    first_move = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Board(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    num_cols = models.IntegerField
    num_rows = models.IntegerField


class Game(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

