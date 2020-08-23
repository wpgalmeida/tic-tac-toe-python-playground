import uuid

from django.db import models

# Create your models here.
from tic_tac_toe_python_playground.apps.core.dealer import mark_move
from tic_tac_toe_python_playground.apps.core.game_builder import create_board
from tic_tac_toe_python_playground.apps.core.jugde import check_end_game


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
    # num_cols = models.IntegerField()
    num_rows = models.IntegerField()

    def save(self, *args, **kwargs):
        if not num_row_is_valid(self.num_rows):
            raise ValueError("Numero de linhas deve ser entre 3 e 6")
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.


def symbol_is_valid(symbol, board):
    last_pb = PlayerBoard.objects.last()
    if last_pb != None:
        if last_pb.symbol == symbol and last_pb.board == board:
            return False
    return True


class PlayerBoard(StandardModelMixin):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    symbol = models.CharField(max_length=1, blank=False, default=None)

    def save(self, *args, **kwargs):
        if not symbol_is_valid(self.symbol, self.board):
            raise ValueError("Escolha outro simbolo")
        else:
            super().save(*args, **kwargs)  # Call the "real" save() method.

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


def _fill_board_with_all_movements(board, player, position):
    qs_movements = Movements.objects.filter(board=board)
    size_qs = qs_movements.all().count()
    board_data = Board.objects.filter(id=board.id).get()
    board_to_check = create_board(board_data.num_rows)

    if size_qs > 0:
        for i in range(0, size_qs):
            movement = qs_movements[i]
            pb_data = PlayerBoard.objects.filter(
                board=movement.board, player=movement.player
            ).get()
            board_to_check = mark_move(
                board_to_check, pb_data.symbol, movement.position
            )

    return board_to_check


def _check_end_game(board, player, position):
    # old movements
    board_to_check = _fill_board_with_all_movements(board, player, position)
    # actual movement
    pb_data = PlayerBoard.objects.filter(board=board, player=player).get()
    board_to_check = mark_move(board_to_check, pb_data.symbol, position)

    check_end_game(board_to_check)


class Movements(StandardModelMixin):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    position = models.IntegerField()

    def save(self, *args, **kwargs):
        _check_end_game(self.board, self.player, self.position)
        super().save(*args, **kwargs)  # Call the "real" save() method.

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["position", "board"], name="unique_position_board"
            )
        ]
