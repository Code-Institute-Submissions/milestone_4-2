from django.contrib import admin
from .models import UserProfile


# Register your models here.

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin) :
    list_display = ['username', 'email']
