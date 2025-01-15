from django.urls import path
from .views import ProductListView, UpdateTrackingView

urlpatterns = [
    path('product', ProductListView.as_view(), name='product-list'),
    path('products/<int:product_id>/track/', UpdateTrackingView.as_view(), name='update-tracking'),
]
