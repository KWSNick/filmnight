from django.shortcuts import get_object_or_404
from films.models import film


def basket_contents(request):

    basket_items = []
    basket = request.session.get('basket', {})

    for film_id in basket.items():
        film_id[1]['digital_total'] = 0
        film_id[1]['dvd_total'] = 0
        film_id[1]['br_total'] = 0
        Film = get_object_or_404(film, pk=film_id[0])
        film_id[1]['digital_total'] += film_id[1]['digital'] * 3.99
        film_id[1]['dvd_total'] += film_id[1]['dvd'] * 5.99
        film_id[1]['br_total'] += film_id[1]['bluray'] * 7.99
        basket_items.append({
            'film_id': film_id[0],
            'film': Film,
            'format_quantity': {'digital': film_id[1]['digital'],
                                'dvd': film_id[1]['dvd'],
                                'bluray': film_id[1]['bluray']},
            'format_total_cost': {'digital_total': film_id[1]['digital_total'],
                                  'dvd_total': film_id[1]['dvd_total'],
                                  'br_total': film_id[1]['br_total']}
        })

    dvd_quantity = 0
    br_quantity = 0
    for item in basket_items:
        dvd_quantity += int(item['format_quantity']['dvd'])
        br_quantity += int(item['format_quantity']['bluray'])

    if dvd_quantity > 0 or br_quantity > 0:
        delivery = 2.99
    else:
        delivery = 0.00

    digital_subtotal = 0
    dvd_subtotal = 0
    br_subtotal = 0
    for item in basket_items:
        digital_subtotal += float(
            item['format_total_cost']['digital_total'])
        dvd_subtotal += float(item['format_total_cost']['dvd_total'])
        br_subtotal += float(item['format_total_cost']['br_total'])

    total = digital_subtotal + dvd_subtotal + br_subtotal

    grand_total = delivery + total

    context = {
        'basket_items': basket_items,
        'digital_subtotal': digital_subtotal,
        'dvd_subtotal': dvd_subtotal,
        'br_subtotal': br_subtotal,
        'total': total,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
