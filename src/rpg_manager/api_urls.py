from django.urls import path

from . import views

app_name = "rpg_manager_api"
urlpatterns = [
    path("", views.api_index, name="rpg_api_index"),
    path("player/<int:pk>", views.player_api, name="player_api"),
]
