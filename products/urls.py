from django.urls import path
from .views import *

urlpatterns = [
    path("", ProductListView.as_view(), name="all_products"),
    path("product/<int:pk>/", ProductDetailView.as_view(), name="one_product"),
    path("product/add/", ProductCreateView.as_view(), name="add_product"),
    path("product/<int:pk>/edit/", ProductUpdateView.as_view(), name="edit_product"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="delete_product"),

    path("all_categories/", CategoryListView.as_view(), name="all_categories"),
    path("category/<int:pk>/", CategoryDetailView.as_view(), name="category_page"),
    path("category/add/", CategoryCreateView.as_view(), name="add_category"),
    path("category/<int:pk>/edit/", CategoryUpdateView.as_view(), name="edit_category"),
    path("category/<int:pk>/delete/", CategoryDeleteView.as_view(), name="delete_category"),
    path("cart/<int:pk>/", create_cart, name="create_cart"),    
    path("cart_detail" , DetailCart.as_view() , name="detail_cart"),
    path("cart/remove/<int:pk>/", remove_from_cart, name="remove_from_cart"),
]
