from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import film
from basket.models import price_list
from profiles.models import users
from .forms import priceForm, filmForm

# Create your views here.


def index(request):
    """ A view which returns the main films page """

    films = film.objects.all()
    query = None
    if request.user.is_authenticated:
        profile = users.objects.get(user=request.user)
    else:
        profile = {}

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('films'))

        Queries = Q(Series_Title__icontains=query)
        films = films.filter(Queries)

    context = {
        'films': films,
        'profile': profile,
        'search_term': query,
    }

    if request.user.is_authenticated:
        return render(request, 'films/index.html', context)
    else:
        return redirect('accounts/login/')


def filmpage(request, film_id):
    """ A view which returns the film detail page """
    if request.user.is_authenticated:
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

        return render(request, 'films/filmpage.html', context)

    else:
        return redirect(reverse('films'))


def watch(request, film_id):
    """ A view which would host the digital streaming media """
    if request.user.is_authenticated:
        Film = get_object_or_404(film, pk=film_id)
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
        }

        if digital_value == 0:
            return render(request, 'films/comingsoon.html', context)
        else:
            messages.error(request, "You haven't purchased this\
                           title digitally yet.")
            return redirect(reverse('films'))


def admin_area(request):
    """ A view to access admin functions """

    if request.user.is_superuser:
        prices = price_list.objects.all()
        films = film.objects.all()
        query = None
        template = 'films/admin.html'

        if request.GET:
            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    return redirect(reverse('admin_area'))

            Queries = Q(Series_Title__icontains=query)
            films = films.filter(Queries)

        context = {
            'prices': prices,
            'films': films,
            'search_term': query,
        }

        return render(request, template, context)
    else:
        messages.error(request, 'You are not authorised to access this area.')
        return redirect(reverse('films'))


def edit_price(request, price_id):
    """ A view to a price edit form """
    if request.user.is_superuser:
        print('Price ID is', price_id)

        price = get_object_or_404(price_list, pk=price_id)

        if not request.user.is_superuser:
            messages.error(request,
                           'You are not authorised to access this area.')
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

        return render(request, template, context)

    else:
        messages.error(request, 'You are not authorised to access this area.')
        return redirect(reverse('films'))


def add_film(request):
    """ Add a new film to the site """
    if request.user.is_superuser:
        if request.method == 'POST':
            form = filmForm(request.POST, request.FILES)
            if form.is_valid:
                form.save()
                messages.success(request, 'Film added successfully!')
                return redirect(reverse('admin_area'))
            else:
                messages.error(request, 'Failed to add film, check your data.')
        else:
            form = filmForm()

        template = 'films/add_film.html'
        context = {
            'form': form,
        }

        return render(request, template, context)

    else:
        messages.error(request, 'You are not authorised to access this area.')
        return redirect(reverse('films'))


def edit_film(request, film_id):
    """Edit a films details"""
    if request.user.is_superuser:
        Film = get_object_or_404(film, pk=film_id)
        if request.method == 'POST':
            form = filmForm(request.POST, request.FILES, instance=Film)
            if form.is_valid:
                form.save()
                messages.success(request,
                                 f'{Film.Series_Title} successfully Updated!')
                return redirect(reverse('admin_area'))
            else:
                messages.error(request, 'Failed to add film, check your data.')
        else:
            form = filmForm(instance=Film)

        template = 'films/edit_film.html'

        context = {
            'form': form,
            'film': Film,
        }

        return render(request, template, context)

    else:
        messages.error(request, 'You are not authorised to access this area.')
        return redirect(reverse('films'))


def delete_film(request, film_id):
    if request.user.is_superuser:
        Film = get_object_or_404(film, pk=film_id)
        Film.delete()
        messages.success(request, f'{Film.Series_Title} Deleted!')
        return redirect(reverse('admin_area'))
    else:
        messages.error(request, 'You are not authorised to access this area.')
        return redirect(reverse('films'))
