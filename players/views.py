from django.shortcuts import render
from django.views.generic import ListView

from .models import Player


class PlayerListView(ListView):
    template_name = 'players/list_of_players.html'
    model = Player
    context_object_name = 'all_players'
