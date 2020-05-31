from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from tic_tac_toe_python_playground.apps.core.drf import views

urlpatterns = [
    path("api-players/", views.PlayerList.as_view()),
    path("api-players/<str:pk>/", views.PlayerDetail.as_view()),
    path("api-boards/", views.BoardList.as_view()),
    path("api-board/<str:pk>/", views.BoarDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
