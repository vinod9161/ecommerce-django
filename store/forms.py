# forms.py

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'slug', 'price', 'description', 'image', 'stock', 'is_available', 'category']
