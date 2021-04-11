from django.shortcuts import render, redirect, HttpResponse
from films.models import film
from .models import price_list

# Create your views here.


def view_basket(request):
    """A view to see all items in the basket"""

    films = film.objects.all()
    prices = price_list.objects.all()

    context = {
        'films': films,
        'prices': prices,
    }

    return render(request, 'basket/basket.html', context)


def add_to_basket(request, film_id):
    """Add films to the basket in various formats"""

    dig_quantity = int(request.POST.get('dig_quantity'))
    dvd_quantity = int(request.POST.get('dvd_quantity'))
    br_quantity = int(request.POST.get('br_quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if film_id in list(basket.keys()):
        basket[film_id]['digital'] = 1
        basket[film_id]['dvd'] = dvd_quantity
        basket[film_id]['bluray'] = br_quantity
    else:
        basket[film_id] = {'digital': dig_quantity,
                           'dvd': dvd_quantity,
                           'bluray': br_quantity}

    request.session['basket'] = basket
    return redirect(redirect_url)


def remove_from(request, film_id):
    """Remove the item from the basket"""

    try:
        basket = request.session.get('basket', {})
        print(basket)
        basket.pop(film_id)
        request.session['basket'] = basket
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(status=500)
