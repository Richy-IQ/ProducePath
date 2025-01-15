from django.contrib import admin

# Register your models here.
from django.contrib import admin
from order.models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'consumer', 'product', 'quantity', 'status', 'created_at', 'last_updated')
    search_fields = ('consumer__username', 'product__name')
    list_filter = ('status', 'created_at')
    ordering = ('id',)
