from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('date','order_total',)

    fields = ('date', 'full_name', 'email', 'phone_number', 
                'product', 'order_total',)

    list_display = ('date', 'full_name', 'product', 'order_total')

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
