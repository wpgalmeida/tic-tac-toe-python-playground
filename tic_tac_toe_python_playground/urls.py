"""tic_tac_toe_python_playground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from tic_tac_toe_python_playground.apps.core.drf import views
from tic_tac_toe_python_playground.apps.core.views import MyView, GameView

router = routers.DefaultRouter()
router.register(r"player", views.PlayerViewSet)
router.register(r"board", views.BoardViewSet)
router.register(r"player-board", views.PlayerBoardViewSet)
router.register(r"game", views.GameViewSet)
router.register(r"movement", views.MovementsViewSet)

router_v2 = routers.DefaultRouter()
router_v2.register(r"player", views.PlayerViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-world/", MyView.as_view()),
    path("", include("tic_tac_toe_python_playground.apps.core.drf.urls")),
    # Urls DRF v1
    path("api/v1/", include(router.urls)),
    path("api/v2/", include(router_v2.urls)),
]
