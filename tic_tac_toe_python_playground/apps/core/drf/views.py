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

        custom_serializer = serializer.validated_data
        board_id = str(custom_serializer["board"].id)
        player = custom_serializer["player"]
        position_moved = custom_serializer["position"]
        available_positions = check_and_evaluate_available_positions(board_id)

        # Validar jogador não é o mesmo do ultimo movimento
        last_movement: Movements = self.queryset.order_by("created_at").last()
        if last_movement is not None and last_movement.player == player:
            headers = self.get_success_headers(serializer.data)
            view_serializer = serializer.data
            view_serializer["PlayerMoveIs"] = "Não é a sua vez"
            return Response(view_serializer, status=status.HTTP_400_BAD_REQUEST, headers=headers)

        # Validar posicao valida
        if position_moved not in available_positions:
            headers = self.get_success_headers(serializer.data)
            view_serializer = serializer.data
            view_serializer["availableMovements"] = available_positions
            return Response(view_serializer, status=status.HTTP_400_BAD_REQUEST, headers=headers)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        view_serializer = serializer.data
        return Response(view_serializer, status=status.HTTP_201_CREATED, headers=headers)


def check_and_evaluate_available_positions(board_id):
    done_movements = []
    available_movements = []

    board: Board = Board.objects.filter(id=board_id).get()
    max_position = board.num_cols * board.num_rows
    mv: Movements = Movements.objects.filter(board_id=board_id)

    list_of_movements = list(mv)

    for ind in range(0, len(list_of_movements)):
        done_movements.append(list_of_movements[ind].position)

    for pos in range(0, max_position):
        if pos not in done_movements:
            available_movements.append(pos)

    return available_movements
