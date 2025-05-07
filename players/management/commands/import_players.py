import csv
from django.core.management.base import BaseCommand
from players.models import Player

class Command(BaseCommand):
    help = 'Importă jucători ATP din fișierul CSV'

    def handle(self, *args, **kwargs):
        with open('tennis_atp/atp_players.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                first = row['name_first'].strip()
                last = row['name_last'].strip()
                country = row.get('ioc', 'Unknown')

                Player.objects.get_or_create(
                    first_name=first,
                    last_name=last,
                    defaults={
                        'country': country,
                        'age': 0
                    }
                )
        self.stdout.write(self.style.SUCCESS('✅ Import complet!'))
