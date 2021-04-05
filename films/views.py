from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    """ A view which returns the main films page """
    if request.user.is_authenticated:
        return render(request, 'films/index.html')
    else:
        return redirect('accounts/login/')
