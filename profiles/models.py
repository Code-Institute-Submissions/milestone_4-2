from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField

class UserProfile(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f'Profile for Username {self.username}'

