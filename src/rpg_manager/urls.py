from django.urls import path
from django.urls import include
from . import views
from . import api_urls

app_name = "rpg_manager"
urlpatterns = [
    path("", views.RpgIndexView.as_view(), name="index"),
    path("player/<int:pk>", views.DetailView.as_view(), name="player-detail"),
    path("characters/create", views.CreateChar.as_view(), name="create-char"),
    path("characters/edit/<int:pk>", views.EditChar.as_view(), name="edit-char"),
    path("characters/<int:pk>", views.CharacterDetail.as_view(), name="char-detail"),
    path("api/", include(api_urls)),
]
