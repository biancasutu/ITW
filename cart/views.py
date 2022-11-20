from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from cart.forms import CartForm
from cart.models import ShoppingCart
from store.models import StoreClothes, StoreAccessories


def create_cart_product(request):
    if request.method == 'POST':
        print(request.POST.get('clothes_id'))
        cloth = StoreClothes.objects.get(id=int(request.POST.get('clothes_id')))
        cart_clothes = ShoppingCart(
            clothes_id=cloth,
            number_of_products_added=1,
            price=cloth.price,
            clothes_size=cloth.size
        )
        cart_clothes.save()
    return redirect('all_products')


def create_cart_product_acc(request):
    if request.method == 'POST':
        print(request.POST.get('clothes_id'))
        cloth = StoreAccessories.objects.get(id=int(request.POST.get('clothes_id')))
        cart_clothes = ShoppingCart(
            clothes_id=cloth,
            number_of_products_added=1,
            price=cloth.price,
            clothes_size=cloth.size
        )
        cart_clothes.save()
    return redirect('all_products')


class CartCreateView(CreateView):
    template_name = 'cart/add_to_cart.html'
    model = ShoppingCart
    form_class = CartForm
    success_url = reverse_lazy('add_to_cart')


class CartListView(ListView):
    template_name = 'cart/show_cart.html'
    model = ShoppingCart
    context_object_name = 'cart_items'


class CartUpdateView(UpdateView):
    template_name = 'cart/update_cart.html'
    model = ShoppingCart
    form_class = CartForm
    context_object_name = 'cart_items'


class CartDeleteView(DeleteView):
    template_name = 'cart/delete_cart.html'
    model = ShoppingCart
    success_url = ''
