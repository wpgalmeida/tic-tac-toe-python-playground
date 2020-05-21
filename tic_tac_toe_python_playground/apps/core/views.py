from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render

# Create your views here.
from tic_tac_toe_python_playground.apps.core.models import Game, Board


class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


class GameView(View):
    def get(self, request, *args, **kwargs):
        games = Game.objects.all()
        my_dict = {"games": list(games.values())}

        return JsonResponse(my_dict)
