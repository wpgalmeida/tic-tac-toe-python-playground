from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tic_tac_toe_python_playground.apps.core.drf import views

urlpatterns = [
    # Url for Player
    path("api-players/", views.PlayerList.as_view()),
    path("api-players/<str:pk>/", views.PlayerDetail.as_view()),
    # Url for Board
    path("api-boards/", views.BoardList.as_view()),
    path("api-board/<str:pk>/", views.BoardDetail.as_view()),
    # Url for PlayerBoard
    path("api-player-board/", views.PlayerBoardList.as_view()),
    path("api-player-board/<str:pk>/", views.PlayerBoardDetail.as_view()),
    # Url for Game
    path("api-games/", views.GameList.as_view()),
    path("api-game/<str:pk>/", views.GameDetail.as_view()),
    # Url for Movement
    path("api-movements/", views.MovementList.as_view()),
    path("api-movemet/<str:pk>/", views.MovementsDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
