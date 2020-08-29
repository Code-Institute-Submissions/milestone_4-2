from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm
from products.models import Training

import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request, pk):
    product = Training.objects.get(id=pk)

    if request.method == "POST":
        if 'cancel' in request.POST:
            return redirect(reverse('products'))
        payment_form = MakePaymentForm(request.POST)

        if payment_form.is_valid():

            try:
                # stripe takes integer amount so need to multiply from cents up
                customer = stripe.Charge.create(
                    amount=int(product.price * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Sorry, your card was declined.")
                return render(request, "checkout_fail.html")

            if customer.paid:
                messages.success(request, "You have successfully paid")
                return render(request, "checkout_success.html")

            else:
                messages.error(request, "Unable to take payment")
                return render(request, "checkout_fail.html")

        else:
            payment_form = MakePaymentForm()

    else:
        payment_form = MakePaymentForm()

    payment_form = MakePaymentForm
    return render(request, "checkout.html",
                  {'payment_form': payment_form,
                   "publishable": settings.STRIPE_PUBLISHABLE,
                   'product': product, })
