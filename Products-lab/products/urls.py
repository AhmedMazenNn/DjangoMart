from django.urls import path
from .views import all_products_page , view_product ,category_page ,all_categories_page

urlpatterns = [
    path("all_products/", all_products_page, name="all_products"),
    path("<int:product_id>/", view_product, name="one_product"),
    path("category/<int:category_id>/", category_page, name="category_page"),
    path("all_categories/", all_categories_page, name="all_categories"),
]
