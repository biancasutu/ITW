from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    number_of_titles = models.IntegerField()
    gender = models.CharField(max_length=30)
    # player_id = models.IntegerField(unique=True)  # de fiecare data cand fac update la datele din api va verifica
                                            # sa nu am duplicate(sa nu imi insereze iar un obiect pe care deja il am)
