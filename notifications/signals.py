from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Order
from .models import Notification

@receiver(post_save, sender=Order)
def notify_consumer(sender, instance, created, **kwargs):
    if not created and instance.status == "Delivered":
        message = f"Your order #{instance.id} for {instance.product.name} has been delivered!"
        Notification.objects.create(message=message, recipient=instance.consumer.email)