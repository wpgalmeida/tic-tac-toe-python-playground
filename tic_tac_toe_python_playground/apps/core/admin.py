from django.contrib import admin

# Register your models here.
from tic_tac_toe_python_playground.apps.core.models import Player

admin.site.register(Player)
