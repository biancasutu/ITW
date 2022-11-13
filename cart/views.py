from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from cart.forms import CartForm
from cart.models import Cart


class CartCreateView(CreateView):
    template_name = 'cart/add_to_cart.html'
    model = Cart
    form_class = CartForm
    success_url = reverse_lazy('add_to_cart')


class CartListView(ListView):
    template_name = 'cart/show_cart.html'
    model = Cart
    context_object_name = 'cart_items'


class CartUpdateView(UpdateView):
    template_name = 'cart/update_cart.html'
    model = Cart
    form_class = CartForm
    context_object_name = 'cart_items'

