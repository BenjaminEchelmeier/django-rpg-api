from django.contrib import admin
from .models import Player


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Player
    extra = 1


admin.site.register(Player)
