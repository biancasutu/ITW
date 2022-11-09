from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
import requests

from .models import StoreClothes, StoreAccessories


class ClothesCreateView(CreateView):
    template_name = 'store/create_clothes.html'
    model = StoreClothes
    fields = ''
    success_url = reverse_lazy('create_clothes')


class ClothesDeleteView(DeleteView):
    model = StoreClothes
    template_name = ''


class ClothesUpdateView(UpdateView):
    model = StoreClothes
    template_name = ''


class StoreClothesListView(ListView):
    template_name = 'store/clothes.html'
    model = StoreClothes
    context_object_name = 'clothes'

    def get(self, request, *args, **kwargs):
        if not self.kwargs.get('prod_type'):
            context = StoreClothes.objects.filter(gender=self.kwargs['gender'])
            return render(request, 'store/clothes.html', {'clothes': context})

        context = StoreClothes.objects.filter(gender=self.kwargs['gender'], prod_type=self.kwargs['prod_type'])
        # daca cheia prod_type contine substringul 'all' (din urls) se executa select all (daca se intra in if)

        return render(request, 'store/clothes.html', {'clothes': context})


def get_filtered(request, acc_name):
    if acc_name in ['Rackets', 'Headbands']:
        context = StoreAccessories.objects.filter(prod_type=acc_name)
        return render(request, 'store/accessories.html', {'all_accessories': context})

    context = StoreAccessories.objects.all()

    return render(request, 'store/accessories.html', {'all_accessories': context})


