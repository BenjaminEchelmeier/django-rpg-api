from django.urls import path

from . import views

app_name = "rpg_manager_api"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("player/<int:pk>/", views.DetailView.as_view(), name="player_detail"),
]
