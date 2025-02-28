from django.shortcuts import render ,get_object_or_404
from .models import Product , Category

# Create your views here.
def all_products_page(request):
    products = Product.objects.all()
    return render(request, 'all_products.html', {'products': products})

def view_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, "single_product.html", {"product": product})


def all_categories_page(request):
    categories = Category.objects.all()
    return render(request, "all_categories.html", {"categories": categories})

def category_page(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, "category.html", {
        "category": category,
        "products": products,
    })