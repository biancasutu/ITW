from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
import requests

from .models import StoreClothes, StoreAccessories


class StoreClothesListView(ListView):
    template_name = 'store/all_products.html'
    model = StoreClothes
    context_object_name = 'all_products'

    # def get_context_data(self, *, object_list=None, **kwargs):

    def get(self, request, *args, **kwargs):
        if not self.kwargs.get('prod_type'):
            context = StoreClothes.objects.filter(gender=self.kwargs['gender'])
            return render(request, 'store/all_products.html', {'all_products': context})

        context = StoreClothes.objects.filter(gender=self.kwargs['gender'], prod_type=self.kwargs['prod_type'])
        # daca cheia prod_type contine substringul 'all' (din urls) se executa select all (daca se intra in if)

        return render(request, 'store/all_products.html', {'all_products': context})


def get_filtered(request, acc_name):
    if acc_name in ['Rackets','Headbands']:
        context = StoreAccessories.objects.filter(prod_type=acc_name)
        return render(request, 'store/accessories.html', {'all_accessories': context})

    context = StoreAccessories.objects.all()

    return render(request, 'store/accessories.html', {'all_accessories': context})
