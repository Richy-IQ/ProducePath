from django.db import models
from django.conf import settings


class Farmer(models.Model):
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=100)

class Product(models.Model):
    CATEGORY_CHOICES = [
        ("fruit", "Fruit"),
        ("vegetable", "Vegetable"),
        ("grain", "Grain"),
        ("dairy", "Dairy"),
        ("meat", "Meat"),
    ]
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity_available = models.IntegerField()

    def __str__(self):
        return self.name

class ProductTracking(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="tracking_records")
    status = models.CharField(max_length=50, choices=[
        ('harvested', 'Harvested'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
    ])
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
