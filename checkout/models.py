import uuid

from django.db import models
from products.models import Training

from profiles.models import User


class Order(models.Model):
    product = models.ForeignKey(Training, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    full_name = models.CharField(max_length=50, null=True, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    order_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)


def _make_order_number(self):
    return uuid.uuid4().hex.upper()


def __str__(self):
    return f'pk {self.product.name} on order {self.order.product.price}'
