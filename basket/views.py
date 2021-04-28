from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from films.models import film
from .models import price_list

# Create your views here.


def view_basket(request):
    """A view to see all items in the basket"""

    films = film.objects.all()
    prices = price_list.objects.all()

    template = 'basket/basket.html'

    context = {
        'films': films,
        'prices': prices,
    }

    if request.user.is_authenticated:
        return render(request, template, context)
    else:
        return redirect(reverse('films'))


def add_to_basket(request, film_id):
    """Add films to the basket in various formats"""
    if request.user.is_authenticated:
        Film = get_object_or_404(film, pk=film_id)
        dig_quantity = int(request.POST.get('dig_quantity'))
        dvd_quantity = int(request.POST.get('dvd_quantity'))
        br_quantity = int(request.POST.get('br_quantity'))
        # redirect_url comes from hidden orderform.html input
        redirect_url = request.POST.get('redirect_url')
        basket = request.session.get('basket', {})

        if dig_quantity < 1 and dvd_quantity < 1 and br_quantity < 1:
            messages.error(request, f'No format quantity added\
                 to basket for {Film.Series_Title}')
            return redirect(reverse('films'))
        else:
            # Update or create a basket item
            if film_id in list(basket.keys()):
                basket[film_id]['digital'] = 1
                basket[film_id]['dvd'] = dvd_quantity
                basket[film_id]['bluray'] = br_quantity
                messages.success(request, f'{Film.Series_Title} Basket Updated')
            else:
                basket[film_id] = {'digital': dig_quantity,
                                'dvd': dvd_quantity,
                                'bluray': br_quantity}
                messages.success(request, f'{Film.Series_Title} Added to Basket')

            request.session['basket'] = basket
            return redirect(redirect_url)
    else:
        return redirect(reverse('films'))


def remove_from(request, film_id):
    """Remove the item from the basket"""
    if request.user.is_authenticated:
        Film = get_object_or_404(film, pk=film_id)
        try:
            basket = request.session.get('basket', {})
            basket.pop(film_id)
            request.session['basket'] = basket
            messages.success(request, f'{Film.Series_Title} Removed Basket')
            return HttpResponse(status=200)
        except Exception as e:
            messages.error(
                request, f'Error removing Item {Film.Series_Title}: {e}')
            return HttpResponse(status=500)
    else:
        return redirect(reverse('films'))
