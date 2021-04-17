from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents

import stripe
import json

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    basket = request.session.get('basket', {})

    if not basket:
        messages.error(request, 'Your shopping basket is empty')
        return redirect(reverse('films/index.html'))

    if request.method == 'POST':
        form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'delivery_add1': request.POST['delivery_add1'],
            'delivery_add2': request.POST['delivery_add2'],
            'delivery_town': request.POST['delivery_town'],
            'delivery_county': request.POST['delivery_county'],
            'delivery_postcode': request.POST['delivery_postcode'],
            'delivery_country': request.POST['delivery_country'],
            'billing_add1': request.POST['billing_add1'],
            'billing_add2': request.POST['billing_add2'],
            'billing_town': request.POST['billing_town'],
            'billing_county': request.POST['billing_county'],
            'billing_postcode': request.POST['billing_postcode'],
            'billing_country': request.POST['billing_country'],
        }

    current_basket = basket_contents(request)
    total = current_basket['grand_total']
    stripe_total = round(total * 100)  # stripe req. integer
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
