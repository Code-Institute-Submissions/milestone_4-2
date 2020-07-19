from django.db import models
from products.models import Training
from django.conf import settings



class Order(models.Model):
    product = models.ForeignKey(Training, null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
    date = models.DateTimeField(auto_now_add=True)
