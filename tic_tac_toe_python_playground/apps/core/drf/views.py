from rest_framework import generics
from tic_tac_toe_python_playground.apps.core.drf.serializers import PlayerSerializer, BoardSerializer
from tic_tac_toe_python_playground.apps.core.models import Player, Board


class PlayerList(generics.ListCreateAPIView):
    """
    API endpoint that allows players to be viewed or edited.
    """

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class BoardList(generics.ListCreateAPIView):
    """
    API endpoint that allows board to be viewed or edited.
    """

    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
