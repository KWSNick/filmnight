from django.shortcuts import render, redirect, get_object_or_404
from .models import film
from basket.models import price_list
from profiles.models import users

# Create your views here.


def index(request):
    """ A view which returns the main films page """

    films = film.objects.all()

    context = {
        'films': films,
    }

    if request.user.is_authenticated:
        return render(request, 'films/index.html', context)
    else:
        return redirect('accounts/login/')


def filmpage(request, film_id):
    """ A view which returns the film detail page """

    Film = get_object_or_404(film, pk=film_id)
    prices = price_list.objects.all()
    profile = users.objects.get(user=request.user)
    for title in profile.purchased_titles.all():
        if title == Film:
            digital_value = 0
            break
        else:
            digital_value = 1

    context = {
        'film': Film,
        'prices': prices,
        'digital_value': digital_value,
    }

    if request.user.is_authenticated:
        return render(request, 'films/filmpage.html', context)
    else:
        return redirect('accounts/login/')
