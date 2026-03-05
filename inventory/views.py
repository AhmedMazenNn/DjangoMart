from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import F
from django.urls import reverse_lazy
from django.contrib import messages
from itertools import chain

from .models import Product
from .forms import ProductForm
from orders.models import Order
from shipment.models import Shipment

from inventory.analytics import build_dashboard_chart


def search_product(request):
    query = request.GET.get("query", "").strip()
    if not query:
        messages.warning(request, "Please enter a product name.")
        return render(request, "inventory/inventory.html", context={"products": [], "query": ""})

    products = Product.objects.filter(name__icontains=query)
    if not products.exists():
        messages.error(request, f"No products found for '{query}'.")

    return render(request, "inventory/inventory.html", context={"products": products, "query": query})


class List_all_products(LoginRequiredMixin, ListView):
    model = Product
    template_name = "inventory/inventory.html"
    context_object_name = "products"
    login_url = "login"
    redirect_field_name = "next"


class Update_product(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/add_product.html"
    success_url = reverse_lazy("list_all")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_name"] = "Update Product"
        context["btn_name"] = "Update_product"
        return context


class create_product(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "inventory/add_product.html"
    success_url = reverse_lazy("list_all")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_name"] = "Add Product"
        context["btn_name"] = "Add_product"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Product created successfully!")
        return response

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields["name"].widget.attrs.update({"autofocus": "autofocus"})
        return form


class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request):
        return render(request, "accounts/dashboard.html")

    def test_func(self):
        return self.request.user.role == "manager"

    def handle_no_permission(self):
        messages.error(self.request, "you have no access to dashboard")
        return redirect("home")

    def post(self, request, query_name):
        context = {
            "shipment_count": Shipment.objects.count(),
            "order_count": Order.objects.count(),
            "product_count": Product.objects.count(),
        }

        chart_div = build_dashboard_chart(
            query_name=query_name,
            Product=Product,
            Shipment=Shipment,
            Order=Order,
        )
        if chart_div:
            context["img"] = chart_div

        return render(request, "accounts/dashboard.html", context)


def approved_info(request):
    orders = Order.objects.select_related("approved_by").values(
        approved_by_name=F("approved_by__username"),
        name=F("supermarket_name"),
        type=F("status"),
    )
    shipments = Shipment.objects.select_related("approved_by").values(
        approved_by_name=F("approved_by__username"),
        name=F("factory_name"),
        type=F("status"),
    )
    combined_records = list(chain(orders, shipments))
    return render(request, "accounts/dashboard.html", {"records": combined_records})