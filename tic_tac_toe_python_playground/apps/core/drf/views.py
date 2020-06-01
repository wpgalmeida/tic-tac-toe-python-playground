from rest_framework import generics
from tic_tac_toe_python_playground.apps.core.drf.serializers import (
    PlayerSerializer,
    BoardSerializer,
    PlayerBoardSerializer,
    GameSerializer,
    MovementsSerializer,
)
from tic_tac_toe_python_playground.apps.core.models import Player, Board, PlayerBoard, Game, Movements


# Views for Player
class PlayerList(generics.ListCreateAPIView):
    """
    API endpoint that allows players to be viewed or edited.
    """

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


# Views for Board
class BoardList(generics.ListCreateAPIView):
    """
    API endpoint that allows board to be viewed or edited.
    """

    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


# Views for PlayerBoard
class PlayerBoardList(generics.ListCreateAPIView):
    """
    API endpoint that allows board to be viewed or edited.
    """

    queryset = PlayerBoard.objects.all()
    serializer_class = PlayerBoardSerializer


class PlayerBoardDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlayerBoard.objects.all()
    serializer_class = PlayerBoardSerializer


# Views for Game
class GameList(generics.ListCreateAPIView):
    """
    API endpoint that allows board to be viewed or edited.
    """

    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


# Views for Movements
class MovementList(generics.ListCreateAPIView):
    """
    API endpoint that allows board to be viewed or edited.
    """

    queryset = Movements.objects.all()
    serializer_class = MovementsSerializer


class MovementsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movements.objects.all()
    serializer_class = MovementsSerializer
