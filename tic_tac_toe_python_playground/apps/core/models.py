import uuid

from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
class StandardModelMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ["-created_at", "-updated_at"]


class Player(StandardModelMixin):
    name = models.CharField(max_length=100, blank=False)
    birth = models.DateField()
    gender = models.CharField(max_length=1, blank=False)  # Male, Female, Others
    bot = models.BooleanField(default=False)

    def __str__(self):
        return self.name


def num_row_is_valid(value):
    if value < 3 or value > 6:
        return False
    return True


class Board(StandardModelMixin):
    # num_rows = models.IntegerField(validators=[validate_num_rows])
    num_rows = models.IntegerField()

    def save(self, *args, **kwargs):
        if not num_row_is_valid(self.num_rows):
            raise ValueError("Numero de linhas deve ser entre 3 e 6")
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.


class PlayerBoard(StandardModelMixin):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=1, blank=False, default=None)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["player", "board"], name="unique_player_board"
            )
        ]


class Game(StandardModelMixin):
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    winner = models.ForeignKey(Player, on_delete=models.CASCADE, null=True)
    draw = models.BooleanField(default=False)


class Movements(StandardModelMixin):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    position = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["position", "board"], name="unique_position_board"
            )
        ]
