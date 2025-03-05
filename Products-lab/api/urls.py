from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)  # API for products
router.register(r'cart', CartViewSet)  # API for cart

urlpatterns = [
    path('', include(router.urls)),  # This will generate routes automatically
]
