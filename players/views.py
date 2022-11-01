from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
import requests
from .models import Player
import json
import http.client


class PlayerListView(View):
    template_name = 'players/list_of_players.html'
    model = Player
    context_object_name = 'all_players'

    def get(self, request, *args, **kwargs):
        import http.client

        conn = http.client.HTTPSConnection("api.sportradar.us")

        conn.request("GET", "/nfl/official/trial/v5/en/games/2019/reg/schedule.xml?api_key={your_api_key}")

        res = conn.getresponse()
        data = res.read()

        print(data.decode("utf-8"))


        # pentru partea de MECIURI LIVE

        # url = "https://ultimate-tennis1.p.rapidapi.com/live_scores"
        # headers = {
        #     "X-RapidAPI-Key": "72038f93cdmshf270f022cac718ep1f42f0jsne3cff1a5275e",
        #     "X-RapidAPI-Host": "ultimate-tennis1.p.rapidapi.com"
        # }
        # response = json.loads(requests.request("GET", url, headers=headers).text)
        # players = []
        # for response_player in response['matches']:
        #     player = Player()
        #     player.gender = response_player['Tournament']
        #     player.first_name = response_player['Tournament']
        #     players.append(player)
        #
        # return HttpResponse(request, players)