from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
import requests


from .models import Store


class StoreListView(ListView):
    template_name = 'store/all_products.html'
    model = Store
    context_object_name = 'all_products'

    # def get_context_data(self, *, object_list=None, **kwargs):



    # def get(self, request, *args, **kwargs):
    #     if 'all' in self.kwargs['prod_type']:
    #         all_products = Store.objects.all()
    #         return HttpResponse(all_products)
    #
    #     all_products = Store.objects.filter(prod_type=self.kwargs['prod_type'])
    #     # daca cheia prod_type contine substringul 'all' (din urls) se executa select all (daca se intra in if)
    #
    #     return HttpResponse(all_products)


