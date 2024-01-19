from celery import shared_task

from order.models import CartItem


@shared_task
def generate_cart():
    CartItem.generate_instances()
