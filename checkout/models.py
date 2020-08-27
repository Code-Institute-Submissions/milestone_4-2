from django.db import models
from django.conf import settings
from products.models import Training
from profiles.models import UserProfile


class Order(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum (item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                                related_name='items',
                                on_delete=models.CASCADE)
    product = models.ForeignKey(Training, 
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
