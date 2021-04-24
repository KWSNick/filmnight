from django import forms
from basket.models import price_list


class priceForm(forms.ModelForm):

    class Meta:
        model = price_list
        exclude = ('cost_name',)
        fields = ('cost_price',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'cost_price': 'Price',
        }
        self.fields['cost_price'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
