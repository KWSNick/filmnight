from django.shortcuts import render, redirect, get_object_or_404
from .models import film

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

    context = {
        'film': Film,
    }

    if request.user.is_authenticated:
        return render(request, 'films/filmpage.html', context)
    else:
        return redirect('accounts/login/')
