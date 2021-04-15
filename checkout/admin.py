from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'user', 'date',
                       'delivery_charge', 'order_charge',
                       'total_charge')
    fields = ('order_number', 'user', 'first_name', 'last_name',
              'email', 'phone_number', 'delivery_add1', 'delivery_add2',
              'delivery_town', 'delivery_county', 'delivery_postcode',
              'delivery_country', 'date', 'delivery_charge',
              'order_charge', 'total_charge')
    list_display = ('order_number', 'last_name',
                    'date', 'total_charge')
    ordering = ('-date',)
