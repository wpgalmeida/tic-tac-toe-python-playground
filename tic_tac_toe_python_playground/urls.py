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
from django.urls import path
from django.urls import include, path
from rest_framework import routers

from tic_tac_toe_python_playground.apps.core import views
from tic_tac_toe_python_playground.apps.core.drf import views
from tic_tac_toe_python_playground.apps.core.views import MyView, SampleGame

router = routers.DefaultRouter()
router.register(r"players", views.PlayerViewSet)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("drf-api/", include(router.urls)),
    path("api/sample/hello-world", MyView.as_view()),
    path("api/sample/test-game", SampleGame.as_view()),
]
