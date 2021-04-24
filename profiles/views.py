from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import users
from .forms import usersForm
from checkout.models import Order
from films.models import film

import json

# Create your views here.


def profile(request):
    if request.user.is_authenticated:
        profile = get_object_or_404(users, user=request.user)
        if request.method == "POST":
            form = usersForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
                messages.success(request,
                                 'Profile details successfully updated!')
            else:
                messages.error(request,
                               "Profile update failed,\
                               please check your details.")
        else:
            form = usersForm(instance=profile)
        orders = profile.orders.all()
        template = 'profiles/profile.html'
        context = {
            'profile': profile,
            'form': form,
            'orders': orders,
        }

        return render(request, template, context)

    else:
        return redirect(reverse('films'))


def orderHistory(request, order_number):
    if request.user.is_authenticated:
        order = get_object_or_404(Order, order_number=order_number)

        messages.info(request, (f'Opened historic order { order_number }.'))

        order_basket = order.basket
        order_basket_doublequotes = order_basket.replace("'", '"')
        order_basket_filmname1 = order_basket_doublequotes.replace("<film:", '"')
        order_basket_filmname2 = order_basket_filmname1.replace(">", '"')
        order_basket_decimal = order_basket_filmname2.replace("Decimal(", '')
        order_basket_bracket = order_basket_decimal.replace(")", '')
        order_basket_json = json.loads(order_basket_bracket)
        films = film.objects.all()
        template = 'checkout/checkout_success.html'
        context = {
            'order': order,
            'order_basket_json': order_basket_json,
            'films': films,
            'from_profile': True,
        }

        return render(request, template, context)

    else:
        return redirect(reverse('films'))
