from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Notification

class NotificationListView(APIView):
    def get(self, request):
        notifications = Notification.objects.filter(read=False)
        data = [{"id": n.id, "message": n.message, "created_at": n.created_at} for n in notifications]
        return Response(data, status=200)

    def post(self, request):
        notification_ids = request.data.get("ids", [])
        Notification.objects.filter(id__in=notification_ids).update(read=True)
        return Response({"message": "Notifications marked as read"}, status=200)
