from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import film
from basket.models import price_list
from profiles.models import users
from .forms import priceForm

# Create your views here.


def index(request):
    """ A view which returns the main films page """

    films = film.objects.all()
    if request.user.is_authenticated:
        profile = users.objects.get(user=request.user)
    else:
        profile = {}

    context = {
        'films': films,
        'profile': profile,
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
    digital_value = 1
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


def watch(request, film_id):
    """ A view which would host the digital streaming media """

    Film = get_object_or_404(film, pk=film_id)

    context = {
        'film': Film,
    }

    if request.user.is_authenticated:
        return render(request, 'films/comingsoon.html', context)
    else:
        return redirect('accounts/login/')


def admin_area(request):
    """ A view to access admin functions """

    prices = price_list.objects.all()
    films = film.objects.all()
    template = 'films/admin.html'

    context = {
        'prices': prices,
        'films': films,
    }

    if request.user.is_superuser:
        return render(request, template, context)
    else:
        return redirect('films/index.html')


def edit_price(request, price_id):
    """ A view to a price edit form """
    print('Price ID is', price_id)

    price = get_object_or_404(price_list, pk=price_id)

    if not request.user.is_superuser:
        messages.error(request, 'You are not authorised to access this area.')
        return redirect('films/index.html')
    
    if request.method == "POST":
        form = priceForm(request.POST, instance=price)
        if form.is_valid():
            form.save()
            messages.success(request, f'{ price.cost_name } successfully\
                             updated!')
            return redirect(reverse('admin_area'))
        else:
            messages.error(request, f'{ price.cost_name } not updated, check\
                           your data entry!')
    else:
        form = priceForm(instance=price)

    template = 'films/edit_price.html'

    context = {
        'price': price,
        'form': form,
    }

    if request.user.is_superuser:
        return render(request, template, context)
    else:
        return redirect('films/index.html')
