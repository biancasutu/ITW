from django.urls import path

from players import views


urlpatterns = [
    path('all', views.PlayerListView.as_view(), name='all_players'),
]
