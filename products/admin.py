from django.contrib import admin
from .models import Training

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        "features",
        "image",
    )

    ordering = ("pk",)

admin.site.register(Training, ProductAdmin)
