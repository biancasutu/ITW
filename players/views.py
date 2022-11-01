from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
import requests
from .models import Player
import json
import http.client


class PlayerListView(ListView):
    template_name = 'players/list_of_players.html'
    model = Player
    context_object_name = 'all_players'

    def get_info_player(self, request, *args, **kwargs):
        def get_players(request):
            all_players = {}
            if 'name' in request.GET:
                name = request.GET['name']
                url ='http://api.sportradar.us/tennis/trial/v3/en/competitors/sr:competitor:89320/profile.json?api_key=dfcrwbyz67sp4ws3jhxhmb73'
                response = requests.get(url)
                data = response.json()
                meals = data['players']
                for player in all_players:
            #         player_data = Player(
            #             name=competitor['strMeal'],
            #             category=i['strCategory'],
            #             instructions=i['strInstructions'],
            #             region=i['strArea'],
            #             slug=i['idMeal'],
            #             image_url=i['strMealThumb']
            #         )
            #         meal_data.save()
            #         all_meals = Meal.objects.all().order_by('-id')
            #
            # return render(request, 'meals/meal.html', {"all_meals":
            #                                                all_meals})




        # import http.client
        #
        # conn = http.client.HTTPSConnection("api.sportradar.us")
        #
        # conn.request("GET", "/nfl/official/trial/v5/en/games/2019/reg/schedule.xml?api_key={your_api_key}")
        #
        # res = conn.getresponse()
        # data = res.read()
        #
        # print(data.decode("utf-8"))




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