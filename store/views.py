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
    form_class = ClothesForm
    success_url = reverse_lazy('clothes')
    permission_required = 'store.add_storeclothes'


class StoreClothesListView(ListView):
    template_name = 'store/clothes.html'
    model = StoreClothes
    context_object_name = 'clothes'

    def get(self, request, *args, **kwargs):
        if self.kwargs:
            if not self.kwargs.get('prod_type'):
                context = StoreClothes.objects.filter(gender=self.kwargs['gender'])
                return render(request, 'store/clothes.html', {'clothes': context})

            context = StoreClothes.objects.filter(gender=self.kwargs['gender'], prod_type=self.kwargs['prod_type'])
            return render(request, 'store/clothes.html', {'clothes': context})
            # daca cheia prod_type contine substringul 'all' (din urls) se executa select all (daca se intra in if)
        context = StoreClothes.objects.all()
        return render(request, 'store/clothes.html', {'clothes': context})


class ClothesUpdateView(UpdateView):
    template_name = 'store/update_clothes.html'
    model = StoreClothes
    form_class = ClothesForm
    success_url = reverse_lazy('clothes')
    # permission_required = 'store.change_storeclothes'


class ClothesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'store/delete_clothes.html'
    model = StoreClothes
    success_url = reverse_lazy('clothes')
    permission_required = 'store.delete_storeclothes'


class AccessoriesCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'store/create_accessories.html'
    model = StoreAccessories
    form_class = AccessoriesForm
    success_url = reverse_lazy('accessories_by_name')
    permission_required = 'store.create_storeaccessories'


class AccessoriesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'store/update_accessories.html'
    model = StoreAccessories
    form_class = AccessoriesForm
    success_url = reverse_lazy('accesories_by_name')
    permission_required = 'store.change_storeaccessories'


class AccessoriesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'store/delete_accessories.html'
    model = StoreAccessories
    success_url = reverse_lazy('accessories_by_name')
    permission_required = 'store.delete_storeaccessories'


def get_filtered(request, acc_name):
    if acc_name in ['Rackets', 'Headbands']:
        context = StoreAccessories.objects.filter(prod_type=acc_name)
        return render(request, 'store/accessories.html', {'all_accessories': context})

    context = StoreAccessories.objects.all()

    return render(request, 'store/accessories.html', {'all_accessories': context})


# class AllProductsView(View):
#     template_name = 'store/all_products.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['clothes'] = StoreClothes.objects.all()
#         context['accessories'] = StoreAccessories.objects.all()

def get_all_products(request):
    clothes = StoreClothes.objects.all()
    accessories = StoreAccessories.objects.all()
    return render(request, 'store/all_products.html', {'clothes': clothes, 'accessories': accessories})
