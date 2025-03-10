from django import forms
from .models import Product, Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ("created_at" , "updated_at" , "tags")

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
