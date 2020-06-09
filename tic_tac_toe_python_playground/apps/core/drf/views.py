from rest_framework import generics, viewsets, status
from rest_framework.response import Response

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


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

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


class BoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

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


class PlayerBoardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

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


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

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


class MovementsViewSet(viewsets.ModelViewSet):
    queryset = Movements.objects.all()
    serializer_class = MovementsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        custom_serializer = serializer.data
        # available_positions = check_and_evaluate_available_positions(custom_serializer["board"]))
        custom_serializer["available_positions"] = str(custom_serializer["board"])

        return Response(custom_serializer, status=status.HTTP_201_CREATED, headers=headers)


def check_and_evaluate_available_positions(board_id):
    pass
