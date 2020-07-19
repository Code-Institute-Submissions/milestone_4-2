from django.shortcuts import render, get_object_or_404, reverse, redirect
from .forms import PaymentForm
from products.models import Training
from .models import Order
from django.contrib import messages


def checkout(request, pk):
    product = Training.objects.get(id=pk)
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect(reverse('products'))
        payment_form = PaymentForm(request.POST)
        order = Order(
            product = product,
            total = order_total
        )

    template = 'checkout/checkout.html'

    return render(request, template)
