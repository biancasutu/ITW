from django.urls import path
from .views import PlayerListView, PlayerDetailView

urlpatterns = [
    path('', PlayerListView.as_view(), name='all_players'),
    path('<int:pk>/', PlayerDetailView.as_view(), name='player_detail'),
]
