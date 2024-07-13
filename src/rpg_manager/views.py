from os import name
from django import forms
from django.shortcuts import render

from django.urls import reverse, reverse_lazy
from django.views import generic
from django.http import HttpResponse, HttpRequest, JsonResponse
from .models import Character, CharacterClass, Player


class CharacterForm(forms.Form):
    name = forms.CharField()


# Create your views here.
def index(request) -> HttpResponse:
    return HttpResponse("hello from index.")


class RpgIndexView(generic.ListView):
    template_name = "rpg_manager/index.html"
    context_object_name = "player_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Player.objects.filter(_is_active=True)


def api_index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Welcome to the API")


def player_api(request: HttpRequest, pk: int) -> HttpResponse:
    if request.method == "POST":
        import ipdb

        ipdb.set_trace()

    else:
        return JsonResponse({"this": "sucks"})


class CreateChar(generic.CreateView):
    model = Character
    fields = ["name", "player", "level"]

    def get_success_url(self) -> str:
        return reverse_lazy("rpg_manager:edit-char", kwargs={"pk": self.object.id})


class ClassSubclassForm(forms.ModelForm):
    class Meta:
        model = CharacterClass
        fields = ["class_type", "level"]


class EditChar(generic.UpdateView):
    model = Character
    form_class = forms.inlineformset_factory(
        Character, CharacterClass, form=ClassSubclassForm
    )

    def get_success_url(self) -> str:
        return reverse_lazy("rpg_manager:char-detail", kwargs={"pk": self.kwargs["pk"]})


class CharacterDetail(generic.DetailView):
    model = Character


class DetailView(generic.DetailView):
    # model = Player
    template_name = "rpg_manager/player_detail.html"
    queryset = Player.objects.all()
    context_object_name = "player"
    # def get_queryset(self):
    #     """
    #     Excludes any questions that aren't published yet.
    #     """
    #     return Player.objects.filter(_is_active=True)
