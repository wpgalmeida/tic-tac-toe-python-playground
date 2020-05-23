from rest_framework import serializers

from tic_tac_toe_python_playground.apps.core.models import Player, Board


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"
