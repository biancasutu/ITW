from django.views.generic import ListView, DetailView
from .models import Player

# Creăm o clasă care extinde ListView și afișează toți jucătorii
class PlayerListView(ListView):
    model = Player  # Modelul pe care îl listăm este Player
    template_name = 'players/list_of_players.html'  # Template-ul HTML folosit pentru afișare
    context_object_name = 'players'  # Numele variabilei în template (folosit în {% for player in players %})

    # Suprascriem metoda get_queryset() pentru a adăuga funcționalitate de căutare
    def get_queryset(self):
        queryset = super().get_queryset()  # Obținem toți jucătorii din baza de date
        query = self.request.GET.get('q')  # Verificăm dacă în URL există parametru de căutare (?q=nume)

        if query:
            # Filtrăm după prenume sau nume, fără diferență între majuscule/micuscule
            queryset = queryset.filter(
                first_name__icontains=query
            ) | queryset.filter(
                last_name__icontains=query
            )
        return queryset  # Returnăm lista filtrată (sau completă, dacă nu s-a căutat nimic)


class PlayerDetailView(DetailView):
    model = Player
    template_name = 'players/player_detail.html'
    context_object_name = 'player'