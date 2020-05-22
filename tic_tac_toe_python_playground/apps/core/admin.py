from django.contrib import admin

# Register your models here.
from tic_tac_toe_python_playground.apps.core.models import Player, Board

admin.site.register(Player)
admin.site.register(Board)
