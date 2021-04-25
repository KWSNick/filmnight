from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name',
                  'email', 'phone_number', 'delivery_add1', 'delivery_add2',
                  'delivery_town', 'delivery_county', 'delivery_postcode',
                  'delivery_country', 'billing_add1', 'billing_add2',
                  'billing_town', 'billing_county', 'billing_postcode',
                  'billing_country')

    def __init__(self, *args, **kwargs):
        """Add placeholders and classes, remove auto labels,
        set autofocus on field 1. Based on CI Boutique Ado
        module."""
        super().__init__(*args, **kwargs)
        placeholders = {
            'first_name': 'First Name',
            'last_name': 'Surname',
            'email': 'Email Address',
            'phone_number': 'Contact Number',
            'delivery_add1': 'Address 1',
            'delivery_add2': 'Address 2',
            'delivery_town': 'Town or City',
            'delivery_county': 'County',
            'delivery_postcode': 'Zip/Postcode',
            'delivery_country': 'Country',
            'billing_add1': 'Billing Address 1',
            'billing_add2': 'Billing Address 2',
            'billing_town': 'Billing Town or City',
            'billing_county': 'Billing County',
            'billing_postcode': 'Billing Zip/Postcode',
            'billing_country': 'Billing Country',
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'delivery_country' or 'billing_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
