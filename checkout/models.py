import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Training
from profiles.models import UserProfile
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator



class Order(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=True, blank=True)
    street_address1 = models.CharField(max_length=80, null=True, blank=True)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=0)
    original_bag = models.TextField(null=True, blank=True, default='')
    stripe_pid = models.CharField(max_length=254, null=True, blank=True, default='')

    product = models.ForeignKey(Training, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=6, decimal_places=2,validators=[
                                             MinValueValidator(0.00),
                                             MaxValueValidator(1500.00)
                                         ])
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} {1} @ {2}".format(self.user.username, self.product.name, self.product.price)



class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=True, blank=True, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Training, null=True, blank=True, on_delete=models.CASCADE)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True, editable=True)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.product.sku} on order {self.order.order_number}'