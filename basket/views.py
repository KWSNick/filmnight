from django.shortcuts import render, redirect
from films.models import film

# Create your views here.


def view_basket(request):
    """A view to see all items in the basket"""

    films = film.objects.all()

    context = {
        'films': films,
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
        basket[film_id]['dvd'] += dig_quantity
        basket[film_id]['bluray'] += br_quantity
    else:
        basket[film_id] = {'digital': dig_quantity,
                           'dvd': dvd_quantity,
                           'bluray': br_quantity}

    request.session['basket'] = basket
    return redirect(redirect_url)
