from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category
from .forms import ProductForm ,CategoryForm
# start products
class ProductListView(ListView): #view all products
    model = Product
    template_name = "all_products.html"
    context_object_name = "products"

class ProductDetailView(DetailView): #view single product
    model = Product
    template_name = "single_product.html"
    context_object_name = "product"
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("all_products")


class ProductUpdateView(UpdateView):  # Update product
    model = Product
    form_class = ProductForm
    template_name = "product_form.html"
    success_url = reverse_lazy("all_products")

class ProductDeleteView(DeleteView): #delete product
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("all_products")

#end product

# start category
class CategoryListView(ListView): #view all categories
    model = Category
    template_name = "all_categories.html"
    context_object_name = "categories"
class CategoryDetailView(DetailView): #view single category
    model = Category
    template_name = "category.html"
    context_object_name = "category"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(category=self.object)  # Filter products by category
        return context

class CategoryCreateView(CreateView):  # Add category
    model = Category
    form_class = CategoryForm 
    template_name = "category_form.html"
    success_url = reverse_lazy("all_categories")

class CategoryUpdateView(UpdateView):  # Update category
    model = Category
    form_class = CategoryForm
    template_name = "category_form.html"
    success_url = reverse_lazy("all_categories")
class CategoryDeleteView(DeleteView): #dalete category
    model = Category
    template_name = "category_confirm_delete.html"
    success_url = reverse_lazy("all_categories")
