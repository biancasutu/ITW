from django import forms
from django.forms import TextInput, DateInput

from cart.models import ShoppingCart, Orders


class CartForm(forms.ModelForm):
    class Meta:
        model = ShoppingCart
        fields = ['clothes_id', 'accessories_id', 'number_of_products_added', 'price', 'clothes_size', 'order_id']

        widgets = {
            'clothes_id': TextInput(attrs={'class': 'form-control'}),
            'accessories_id': TextInput(attrs={'class': 'form-control'}),
            'number_of_products_added': TextInput(attrs={'class': 'form-control'}),
            'price': TextInput(attrs={'class': 'form-control'}),
            'clothes_size': TextInput(attrs={'class': 'form-control'}),
            'order_id': TextInput(attrs={'class': 'form-control'}),
        }


class OrdersForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ['user_id']

        widgets = {
            'user_id': TextInput(attrs={'class': 'form-control'}),
            # 'date_ordered': DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }

