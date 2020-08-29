from django.db import models
from django.conf import settings


class UserProfile(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL,
                                    on_delete=models.CASCADE)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f'Profile for Username {self.username}'
