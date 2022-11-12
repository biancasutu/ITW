from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.sites import requests
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
import requests

from .forms import ClothesForm, AccessoriesForm
from .models import StoreClothes, StoreAccessories


class ClothesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'store/create_clothes.html'
    model = StoreClothes
    fields = ['name_of_product', 'price', 'description_of_product',
              'size', 'prod_type', 'gender']
    success_url = reverse_lazy('create_clothes')
    permission_required = 'clothes.add_clothes'


class StoreClothesListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'store/clothes.html'
    model = StoreClothes
    context_object_name = 'clothes'
    permission_required = 'clothes.clothes_list'

    def get(self, request, *args, **kwargs):
        if not self.kwargs.get('prod_type'):
            context = StoreClothes.objects.filter(gender=self.kwargs['gender'])
            return render(request, 'store/clothes.html', {'clothes': context})

        context = StoreClothes.objects.filter(gender=self.kwargs['gender'], prod_type=self.kwargs['prod_type'])
        # daca cheia prod_type contine substringul 'all' (din urls) se executa select all (daca se intra in if)

        return render(request, 'store/clothes.html', {'clothes': context})


class ClothesUpdateView(UpdateView):
    template_name = 'store/update_clothes.html'
    model = StoreClothes
    form_class = ClothesForm
    success_url = reverse_lazy('clothes')


class ClothesDeleteView(DeleteView):
    template_name = 'store/delete_clothes.html'
    model = StoreClothes
    success_url = reverse_lazy('clothes')


class AccessoriesCreateView(CreateView):
    template_name = 'store/create_accessories.html'
    model = StoreAccessories
    form_class = AccessoriesForm
    success_url = reverse_lazy('accessories_by_name')


class AccessoriesUpdateView(UpdateView):
    template_name = 'store/update_accessories.html'
    model = StoreAccessories
    form_class = AccessoriesForm
    success_url = reverse_lazy('accesories_by_name')


class AccessoriesDeleteView(DeleteView):
    template_name = 'store/delete_accessories.html'
    model = StoreAccessories
    success_url = reverse_lazy('accessories_by_name')


def get_filtered(request, acc_name):
    if acc_name in ['Rackets', 'Headbands']:
        context = StoreAccessories.objects.filter(prod_type=acc_name)
        return render(request, 'store/accessories.html', {'all_accessories': context})

    context = StoreAccessories.objects.all()

    return render(request, 'store/accessories.html', {'all_accessories': context})



