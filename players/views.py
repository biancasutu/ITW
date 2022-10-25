from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
import requests
from .models import Player


class PlayerListView(View):
    template_name = 'players/list_of_players.html'
    model = Player
    context_object_name = 'all_players'

    def get(self, request, *args, **kwargs):
        url = "https://ultimate-tennis1.p.rapidapi.com/live_scores"
        headers = {
            "X-RapidAPI-Key": "SIGN-UP-FOR-KEY",
            "X-RapidAPI-Host": "ultimate-tennis1.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers)
        return HttpResponse(response)

