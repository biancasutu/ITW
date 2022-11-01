from django.urls import path

from players import views


urlpatterns = [
    path('', views.PlayerListView.as_view(), name='all_players'),  # name = identificator pentru template ul din clasa PlayerListView
]
