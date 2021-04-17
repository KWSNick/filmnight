from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from basket.contexts import basket_contents
from films.models import film
from .models import Order

import stripe
import json

# Create your views here.


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'basket': json.dumps(request.session.get('basket', {})),
            'save_delivery': request.POST.get('save_delivery'),
            'save_billing': request.POST.get('save_billing'),
            'username': request.user,
        })
        messages.success(request, 'cache_checkout_data success')
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request,
                       'Your payment cannot be processed, please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    basket = request.session.get('basket', {})

    current_basket = basket_contents(request)
    delivery = current_basket['delivery']
    order_total = current_basket['total']
    total = current_basket['grand_total']

    if not basket:
        messages.error(request, 'Your shopping basket is empty')
        return redirect(reverse('films/index.html'))

    if request.method == 'POST':
        for item_id in basket.items:
            try:
                Film = film.objects.get(id=item_id)
                messages.success(request, (f'{Film} Added to your collection.'))
            except film.DoesNotExist:
                messages.error(request, (
                    "An item in your basket was not found in our database.\
                    Please try again."
                ))

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
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.basket = json.dumps(basket)
            order.delivery_charge = delivery
            order.order_charge = order_total
            order.total_charge = total
            order.save()
            request.session['save_delivery'] = 'save_delivery' in request.POST
            request.session['save_billing'] = 'save_billing' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, "Error detected in your details.\
                correct to process your order.")

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
    print(intent)
    print(context)

    return render(request, template, context)

def checkout_success(request, order_number):
    """Handle successful checkouts"""
    save_delivery = request.session.get('save_delivery')
    save_billing = request.session.get('save_billing')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order {order_number} successfully processed.')

    if basket in request.session:
        del request.session['basket']
    
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
