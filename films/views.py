from django.shortcuts import render, redirect
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
