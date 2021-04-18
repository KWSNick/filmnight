from django.shortcuts import get_object_or_404
from films.models import film
from .models import price_list
from decimal import Decimal, ROUND_DOWN


def basket_contents(request):

    basket_items = []
    basket = request.session.get('basket', {})
    digital_cost_obj = get_object_or_404(price_list, cost_name='digital')
    dvd_cost_obj = get_object_or_404(price_list, cost_name='dvd')
    bluray_cost_obj = get_object_or_404(price_list, cost_name='bluray')

    for film_id in basket.items():
        film_id[1]['digital_total'] = 0
        film_id[1]['dvd_total'] = 0
        film_id[1]['br_total'] = 0
        Film = get_object_or_404(film, pk=film_id[0])
        film_id[1]['digital_total'] += film_id[1]['digital'] * float(
                                                digital_cost_obj.cost_price)
        film_id[1]['dvd_total'] += film_id[1]['dvd'] * float(
                                                dvd_cost_obj.cost_price)
        film_id[1]['br_total'] += film_id[1]['bluray'] * float(
                                                bluray_cost_obj.cost_price)
        basket_items.append({
            'film_id': film_id[0],
            'film': Film,
            'format_quantity': {'digital': film_id[1]['digital'],
                                'dvd': film_id[1]['dvd'],
                                'bluray': film_id[1]['bluray']},
            'format_total_cost': {'digital_total': Decimal(
                                        film_id[1]['digital_total']).quantize(
                                        Decimal('1.00'), rounding=ROUND_DOWN),
                                  'dvd_total': Decimal(
                                        film_id[1]['dvd_total']).quantize(
                                        Decimal('1.00'), rounding=ROUND_DOWN),
                                  'br_total': Decimal(
                                        film_id[1]['br_total']).quantize(
                                        Decimal('1.00'), rounding=ROUND_DOWN)}
        })

    dvd_quantity = 0
    br_quantity = 0
    for item in basket_items:
        dvd_quantity += int(item['format_quantity']['dvd'])
        br_quantity += int(item['format_quantity']['bluray'])

    delivery_object = get_object_or_404(price_list, cost_name='delivery')

    if dvd_quantity > 0 or br_quantity > 0:
        delivery = float(delivery_object.cost_price)
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

    grand_total = Decimal(delivery + total).quantize(
                                        Decimal('1.00'), rounding=ROUND_DOWN)

    context = {
        'basket_items': basket_items,
        'digital_subtotal': Decimal(digital_subtotal).quantize(
                                        Decimal('1.00'), rounding=ROUND_DOWN),
        'dvd_subtotal': Decimal(dvd_subtotal).quantize(
                                        Decimal('1.00'), rounding=ROUND_DOWN),
        'br_subtotal': Decimal(br_subtotal).quantize(
                                        Decimal('1.00'), rounding=ROUND_DOWN),
        'total': Decimal(total).quantize(
                                        Decimal('1.00'), rounding=ROUND_DOWN),
        'delivery': Decimal(delivery).quantize(
                                        Decimal('1.00'), rounding=ROUND_DOWN),
        'grand_total': grand_total,
    }

    return context
