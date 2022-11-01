from django.db import models

class Store(models.Model):
    name_of_product = models.CharField(max_length=30)
    price = models.IntegerField()
    description_of_product = models.CharField(max_length=100)
    size = models.CharField(max_length=2)
    number_of_products = models.IntegerField()



