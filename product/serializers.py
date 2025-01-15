from rest_framework import serializers
from .models import Product, ProductTracking

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'farmer', 'description', 'price', 'quantity_available', 'created_at']
        
class ProductTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductTracking
        fields = ['id', 'product', 'status', 'location', 'timestamp', 'updated_by']
        read_only_fields = ['timestamp']