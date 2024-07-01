from django.shortcuts import render

from django.views import generic
from django.http import HttpResponse, HttpRequest
from .models import Player


# Create your views here.
def index(request) -> HttpResponse:
    return HttpResponse("hello from index.")


class IndexView(generic.ListView):
    template_name = "rpg_manager/index.html"
    context_object_name = "player_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.filter(_is_active=True)


def player_api(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        import ipdb

        ipdb.set_trace()


class DetailView(generic.DetailView):
    model = Player
    template_name = "polls/detail.html"

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Player.objects.filter(_is_active=True)
