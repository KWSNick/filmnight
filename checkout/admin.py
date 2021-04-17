from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'user', 'date',
                       'delivery_charge', 'order_charge',
                       'total_charge', 'basket', 'stripe_pid',)
    fields = ('order_number', 'user', 'first_name', 'last_name',
              'email', 'phone_number', 'delivery_add1', 'delivery_add2',
              'delivery_town', 'delivery_county', 'delivery_postcode',
              'delivery_country', 'billing_add1', 'billing_add2',
              'billing_town', 'billing_county', 'billing_postcode',
              'billing_country', 'date', 'basket', 'delivery_charge',
              'order_charge', 'total_charge', 'stripe_pid',)
    list_display = ('order_number', 'last_name',
                    'date', 'total_charge')
    ordering = ('-date',)
