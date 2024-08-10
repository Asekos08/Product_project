from django.urls import path
from .views import ProductDetailView

urlpatterns = [
    path('api/products', ProductDetailView.as_view(), name='product-detail'),
]