from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from cart.forms import CartForm
from cart.models import ShoppingCart
from store.models import StoreClothes, StoreAccessories


def create_cart_product(request, item_id):
    if request.method == 'POST':
        print(request.POST.get('clothes_id'))
        existing_cloth = ShoppingCart.objects.filter(clothes_id_id=item_id).first()
        if existing_cloth:
            existing_cloth.number_of_products_added += 1
            existing_cloth.save()
        else:
            cloth = StoreClothes.objects.get(id=item_id)
            cart_clothes = ShoppingCart(
                clothes_id=cloth,
                number_of_products_added=1,
                price=cloth.price,
                clothes_size=cloth.size
            )
            cart_clothes.save()
    return redirect('all_products')


def create_cart_accesory_item(request, item_id):
    if request.method == 'POST':
        print(request.POST.get('accesories_id'))
        existing_accessory = ShoppingCart.objects.filter(accessories_id_id=item_id).first()
        if existing_accessory:
            existing_accessory.number_of_products_added += 1
            existing_accessory.save()
        else:
            acc = StoreAccessories.objects.get(id=item_id)
            cart_acc = ShoppingCart(
                accessories_id=acc,
                number_of_products_added=1,
                price=acc.price
            )
            cart_acc.save()
    return redirect('all_products')


class CartListView(ListView):
    template_name = 'cart/show_cart.html'
    model = ShoppingCart
    context_object_name = 'cart_items'


class CartUpdateView(UpdateView):
    template_name = 'cart/update_cart.html'
    model = ShoppingCart
    form_class = CartForm
    context_object_name = 'cart/show_cart.html'


def delete_cart_cloth_item(request, clothes_id):
    ShoppingCart.objects.filter(clothes_id_id=clothes_id).first().delete()
    return redirect('show_cart')


def delete_cart_accesory_item(request, accessory_id):
    ShoppingCart.objects.filter(accessories_id_id=accessory_id).first().delete()
    return redirect('show_cart')
