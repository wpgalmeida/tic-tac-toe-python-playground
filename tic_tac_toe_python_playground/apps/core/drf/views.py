from rest_framework import viewsets

from tic_tac_toe_python_playground.apps.core.drf.serializers import PlayerSerializer
from tic_tac_toe_python_playground.apps.core.models import Player


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows players to be viewed or edited.
    """

    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
