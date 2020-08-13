from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Training
import stripe

from django.contrib.auth.models import User
from profiles.models import UserProfile


# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request, pk):
    product = Training.objects.get(pk=pk)
    user = User.objects.get(email=request.user.email)
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect(reverse('products'))
        payment_form = MakePaymentForm(request.POST)
        order_form = OrderForm(request.POST)
        order = Order(
            user=user,
            product=product,
            total=product.price
        )

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(product.price * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
            if customer.paid:
                messages.error(request, "You have successfully paid")
                return redirect(reverse('profile'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    return render(request, "checkout.html", 
                {'order_form': order_form, 
                 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE, 'product': product,
                 'customer': user})
