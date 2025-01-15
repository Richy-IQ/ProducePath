from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order

# Create your views here.
class AnalyticsView(APIView):
    def get(self, request):
        total_orders = Order.objects.count()
        pending_orders = Order.objects.filter(status='Pending').count()
        delivered_orders = Order.objects.filter(status='Delivered').count()

        analytics_data = {
            "total_orders": total_orders,
            "pending_orders": pending_orders,
            "delivered_orders": delivered_orders,
            "delivery_rate": (delivered_orders / total_orders * 100) if total_orders else 0
        }
        return Response(analytics_data, status=200)