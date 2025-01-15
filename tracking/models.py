import uuid
from django.db import models
from django.conf import settings


 

class ProductBatch(models.Model):
    """
    Represents a batch of agricultural products
    """
    PRODUCT_CATEGORIES = (
        ('fruit', 'Fruits'),
        ('vegetable', 'Vegetables'),
        ('grain', 'Grains'),
        ('dairy', 'Dairy'),
        ('meat', 'Meat'),
        ('egg', 'egg'),
        ('chicken','chicken' ),
    )
    
    STATUS_CHOICES = (
        ('harvested', 'Harvested'),
        ('processing', 'Processing'),
        ('in_transit', 'In Transit'),
        ('stored', 'Stored'),
        ('delivered', 'Delivered')
    )
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_type = models.CharField(max_length=50)
    product_category = models.CharField(max_length=20, choices=PRODUCT_CATEGORIES)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    harvest_date = models.DateTimeField()
    current_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    temperature_log = models.JSONField(blank=True, null=True)
    humidity_log = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return f"Batch of {self.product.name} ({self.id})"

class BatchTracking(models.Model):
    """
    Detailed tracking for each product batch
    """
    batch = models.ForeignKey(ProductBatch, on_delete=models.CASCADE)
    location = models.CharField(max_length=300)
    latitude = models.DecimalField(max_digits=10, decimal_places=8)
    longitude = models.DecimalField(max_digits=11, decimal_places=8)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return f"Tracking for {self.batch.id} at {self.location}"
    
# class ProductBatch(models.Model):
#     STATUS_CHOICES = [
#         ("harvested", "Harvested"),
#         ("processing", "Processing"),
#         ("in_transit", "In Transit"),
#         ("stored", "Stored"),
#         ("delivered", "Delivered"),
#     ]

#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     product = models.ForeignKey('product.Product', on_delete=models.CASCADE)
#     quantity = models.DecimalField(max_digits=10, decimal_places=2)
#     harvest_date = models.DateTimeField()
#     current_status = models.CharField(max_length=20, choices=STATUS_CHOICES)
#     temperature_log = models.JSONField(blank=True, null=True)
#     humidity_log = models.JSONField(blank=True, null=True)

#     def __str__(self):
#         return f"Batch of {self.product.name} ({self.id})"

# class BatchTracking(models.Model):
#     batch = models.ForeignKey(ProductBatch, on_delete=models.CASCADE)
#     location = models.CharField(max_length=300)
#     latitude = models.DecimalField(max_digits=10, decimal_places=8)
#     longitude = models.DecimalField(max_digits=11, decimal_places=8)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     operator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return f"Tracking for {self.batch.id} at {self.location}"