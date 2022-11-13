from django import forms
from django.forms import TextInput, Textarea, FileInput

from store.models import StoreClothes, StoreAccessories


class ClothesForm(forms.ModelForm):
    class Meta:
        model = StoreClothes
        # fields = '__all__' # toate fieldurile, ordinea va fi cea din models.py
        fields = ['name_of_product', 'price', 'description_of_product',
                  'size', 'prod_type', 'gender', 'number_of_products', 'image']

        widgets = {
            'name_of_product': TextInput(attrs={'placeholder': 'Product name', 'class': 'form-control'}),
            'price': TextInput(attrs={'placeholder': 'Specify price for product', 'class': 'form-control'}),
            'description_of_product': TextInput(attrs={'placeholder': 'Add some description of the product', 'class': 'form-control'}),
            'size': TextInput(attrs={'placeholder': 'Specify size', 'class': 'form-control'}),
            'prod_type': TextInput(attrs={'placeholder': 'Specify type of product (ex: T-Shirt)', 'class': 'form-control'}),
            'gender': TextInput(attrs={'placeholder': 'Specify gender', 'class': 'form-control'}),
            'number_of_products': TextInput(attrs={'placeholder': 'Specify number of products', 'class': 'form-control'}),
            'image': FileInput(attrs={'class':'form-control'})
        }

        def clean(self):
            self._validate_unique = True
            cleaned_data = self.cleaned_data  # veti avea un dictionar cu toate valorile introduse in formular
            clothes = StoreClothes.objects.filter(name_of_product=cleaned_data['name_of_product']).all() # interogati baza de date unde veti stoca toate hainele salvati in DB
            if clothes is not None:
                return cleaned_data


class AccessoriesForm(forms.ModelForm):
    class Meta:
        model = StoreAccessories
        fields = ['name_of_product', 'price', 'description_of_product', 'prod_type', 'image']

        widgets = {
            'name_of_product': TextInput(attrs={'placeholder': 'Product name', 'class': 'form-control'}),
            'price': TextInput(attrs={'placeholder': 'Specify price for product', 'class': 'form-control'}),
            'description_of_product': Textarea(attrs={'placeholder': 'Add some description of the product', 'class': 'form=control'}),
            'prod_type': TextInput(attrs={'placeholder': 'Specify type of product (ex: T-Shirt)', 'class': 'form-control'}),
            'image': FileInput(attrs={'class': 'form-control'})
        }

