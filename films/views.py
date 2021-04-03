from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view which returns the main films page """
    return render(request, 'films/index.html')
