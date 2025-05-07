from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    country = models.CharField(max_length=3)
    age = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
