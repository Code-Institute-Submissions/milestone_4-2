from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import MakePaymentForm
from .models import Order, OrderLineItem

from products.models import Training
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

@login_required
def checkout(request, pk):
    product = Training.objects.get(id=pk)
    payment_form = MakePaymentForm(request.POST)
    order = Order(
            product=product,
            total=product.price
        )
    if request.method == "POST":

        if payment_form.is_valid():
            try:
                customer = stripe.Charge.create(
                    amount=int(product.price * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                order.save()
                messages.error(request, "Sorry, your card was declined.")
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


    payment_form = MakePaymentForm
    return render(request, "checkout.html",
                  {'payment_form': payment_form, "publishable": settings.STRIPE_PUBLISHABLE, 'product': product,})
