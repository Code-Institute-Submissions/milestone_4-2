from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.models import User

from .forms import MakePaymentForm
from .models import Order, OrderLineItem

from products.models import Training
from profiles.models import UserProfile
from profiles.forms import UserProfileForm

import stripe
import json

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


def checkout(request, pk):
    product = Training.objects.get(id=pk)
    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect(reverse('products'))
            payment_form = MakePaymentForm(request.POST)


            try:
                # stripe takes integer amount so need to multiply from cents up
                customer = stripe.Charge.create(
                    amount=int(product.price * 100),
                    currency="USD",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                # user has not paid, update the Order status
                order.payment_status = 'payment_rejected'
                order.save()
                messages.error(request, "Sorry, your card was declined.")

            if customer.paid:
                # user has paid, update the Order status
                messages.success(request, "Your payment was success and your service level has been updated.")
                order.payment_status = 'payment_collected'
                order.save()
                return redirect(reverse('profile'))

            else:
                messages.success(request, "Please enter your payment information below.")

        else:
            payment_form = MakePaymentForm()

    return render(request, "checkout.html",
                  {'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE, 'product': product,})