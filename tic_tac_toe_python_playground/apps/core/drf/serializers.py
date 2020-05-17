from rest_framework import serializers

from tic_tac_toe_python_playground.apps.core.models import Player


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
