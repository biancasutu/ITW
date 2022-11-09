from django import forms
from django.forms import TextInput

from store.models import StoreClothes


class ClothesForm(forms.ModelForm):
    class Meta:
        model = StoreClothes
        # fields = '__all__' # toate fieldurile, ordinea va fi cea din models.py
        fields = ['name_of_product', 'price', 'description_of_product',
                  'size', 'prod_type', 'gender']

        widgets = {
            'name_of_product': TextInput(attrs={'placeholder': 'Product name', 'class': 'form-control'}),
            'price': TextInput(attrs={'placeholder': 'Specify price for product', 'class': 'form-control'}),
            'description_of_product': TextInput(attrs={'placeholder': 'Add some description of the product', 'class': 'form=control'}),
            'size': TextInput(attrs={'placeholder': 'Specify size', 'class': 'form-control'}),
            'prod_type': TextInput(attrs={'placeholder': 'Specify type of product (ex: T-Shirt)', 'class': 'form-control'}),
            'gender': TextInput(attrs={'placeholder': 'Specify gender', 'class': 'form-control'}),
        }
