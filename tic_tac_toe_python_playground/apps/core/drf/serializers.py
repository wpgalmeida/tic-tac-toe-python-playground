from rest_framework import serializers

from tic_tac_toe_python_playground.apps.core.models import Player, Board, PlayerBoard, Game, Movements


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class PlayerBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerBoard
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = "__all__"


class MovementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movements
        fields = "__all__"
