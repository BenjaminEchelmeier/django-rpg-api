from django.urls import path
from django.urls import include
from . import views

app_name = "rpg_manager"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("api", include("rpg_manager.api_urls")),
    path("player/<int:pk>/", views.DetailView.as_view(), name="player_detail"),
]
