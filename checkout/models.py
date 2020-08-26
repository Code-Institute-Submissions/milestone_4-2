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
    product = models.ForeignKey(Training, null=True, blank=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=6, decimal_places=2,validators=[
                                             MinValueValidator(0.00),
                                             MaxValueValidator(1500.00)
                                         ])
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{0} {1} @ {2}".format(self.user.username, self.product.name, self.product.price)
