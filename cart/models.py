import uuid

from django.contrib.auth.models import User
from django.db import models

from store.models import Product, StoreClothes, StoreAccessories


class Orders(models.Model):  # Bon, tabela cu istoricul comenzilor
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # tabela_coloana -> din tabela user folosesc coloana id
    date_ordered = models.DateTimeField(auto_now=True)


class Cart(models.Model):
    clothes_id = models.ForeignKey(StoreClothes, on_delete=models.CASCADE)
    accessories_id = models.ForeignKey(StoreAccessories, on_delete=models.CASCADE)
    number_of_products_added = models.IntegerField()
    price = models.IntegerField()
    clothes_size = models.CharField(max_length=2)
    order_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    # order_cart = models.ManyToManyField(Orders, on_delete=models.CASCADE)





