from django.urls import reverse_lazy 
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Product, Category , Cart
from .forms import ProductForm ,CategoryForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
    template_name = "products/forms/product_form.html"
    success_url = reverse_lazy("all_products")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.warning(request, "You do not have permission to delete this product.")
            return redirect("all_products")
        return super().dispatch(request, *args, **kwargs)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "products/forms/product_form.html"
    success_url = reverse_lazy("all_products")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.warning(request, "You do not have permission to delete this product.")
            return redirect("all_products")
        return super().dispatch(request, *args, **kwargs)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "product_confirm_delete.html"
    success_url = reverse_lazy("all_products")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.warning(request, "You do not have permission to delete this product.")
            return redirect("all_products")
        return super().dispatch(request, *args, **kwargs)

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
        context["products"] = Product.objects.filter(category=self.object)
        return context

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "products/forms/category_form.html"
    success_url = reverse_lazy("all_categories")

class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "products/forms/category_form.html"
    success_url = reverse_lazy("all_categories")

class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "category_confirm_delete.html"
    success_url = reverse_lazy("all_categories")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.warning(request, "You do not have permission to delete this product.")
            return redirect("all_products")
        return super().dispatch(request, *args, **kwargs)

# end category

@login_required
def create_cart(request, pk):
    product = get_object_or_404(Product, id=pk)

    if not Cart.objects.filter(user=request.user, product=product).exists():
        Cart.objects.create(user=request.user, product=product)
        messages.success(request, f"{product.title} added to cart!")
    else:
        messages.info(request, f"{product.title} is already in your cart.")

    return redirect("all_products")

@login_required
def remove_from_cart(request, pk):
    product = get_object_or_404(Product, id=pk)
    cart_item = Cart.objects.filter(user=request.user, product=product).first()

    if cart_item:
        cart_item.delete()
        messages.success(request, f"{product.title} removed from cart!")
    else:
        messages.warning(request, f"{product.title} was not in your cart.")

    return redirect("all_products")

class DetailCart(LoginRequiredMixin,ListView):
    model = Cart
    template_name = 'cart_detail.html'
    context_object_name = 'cart'
    
    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(user=user).select_related("product")  # Prefetch related products

