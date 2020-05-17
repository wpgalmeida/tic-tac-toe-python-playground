import json

from django.core.serializers import serialize
from django.http import HttpResponse, JsonResponse
from django.views import View

from tic_tac_toe_python_playground.apps.core.models import Game


class MyView(View):
    def get(self, request, *args, **kwargs):

        if request.method == "GET":
            return HttpResponse("Hello, World!")

        return HttpResponse(status=405)


class SampleGame(View):
    def get(self, request, *args, **kwargs):
        games = Game.objects.all()

        my_dict = {"games": list(games.values())}

        return JsonResponse(my_dict)
