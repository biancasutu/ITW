from django.urls import path

from players import views

urlpatterns = [
    path('list-of-players/', views.PlayerListView.as_view(), name='list-of-players'),
]