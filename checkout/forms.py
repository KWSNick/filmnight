from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name',
                  'email', 'phone_number', 'delivery_add1', 'delivery_add2',
                  'delivery_town', 'delivery_county', 'delivery_postcode',
                  'delivery_country',)

    def __init__(self, *args, **kwargs):
        """Add placeholders and classes, remove auto labels,
        set autofocus on field 1. BAsed on CI Boutique Ado
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
        }
        self.fields['first_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
