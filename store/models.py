from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name_of_product = models.CharField(max_length=50)
    price = models.IntegerField()
    description_of_product = models.CharField(max_length=500)
    number_of_products = models.IntegerField()
    image = models.ImageField(default='img_not_found.png')  # pip install Pillow (library pt procesare imagini in python)
    color = models.CharField(max_length=152, default='Black')

    @property
    def availability_status(self):
        if 0 < self.number_of_products < 5:
            return self.number_of_products
        elif self.number_of_products >= 5:
            return 'On Stock'
        return "Out of Stock"

    # availability_status = property(__product_number)


class StoreClothes(Product):
    size = models.CharField(max_length=2)
    prod_type = models.CharField(max_length=40, default='T-Shirt')
    gender = models.CharField(max_length=1, default='M')

    def __str__(self):
        return self.name_of_product


class StoreAccessories(Product):
    prod_type = models.CharField(max_length=40, default='Rackets')

    def __str__(self):
        return self.name_of_product

