from django.contrib import admin

# Register your models here.
from django.contrib import admin
from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_per_unit', 'quantity_available', 'farmer', 'description', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    ordering = ('id',)

