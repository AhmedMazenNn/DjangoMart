from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "price", "rating", "tags", "thumbnail", "category", "cover"]

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
