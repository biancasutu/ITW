from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
import requests
from .models import Store


class StoreListView(View):
    template_name = 'store/all_products.html'
    model = Store
    context_object_name = 'all_products'

    def get(self, request, *args, **kwargs):
        all_products = Store.objects.all()
        return HttpResponse(all_products)

