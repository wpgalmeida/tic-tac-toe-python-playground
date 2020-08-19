import uuid

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


class Board(StandardModelMixin):
    num_cols = models.IntegerField()
    num_rows = models.IntegerField()


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
