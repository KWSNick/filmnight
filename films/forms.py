from django import forms
from basket.models import price_list
from .models import film


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


class filmForm(forms.ModelForm):

    class Meta:
        model = film
        fields = ('Poster_Link', 'Series_Title', 'Released_Year', 'Certificate',
                  'Runtime', 'Genre', 'IMDB_Rating', 'Overview', 'Meta_score',
                  'Director', 'Star1', 'Star2', 'Star3', 'Star4', 'No_of_Votes',
                  'Gross', 'dvd_stock', 'bluray_stock', 'available',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'Poster_Link': 'Poster Image',
            'Series_Title': 'Film Title',
            'Released_Year': 'Year',
            'Certificate': 'Certificate',
            'Runtime': 'Runtime',
            'Genre': 'Genre, entered as a comma separated list',
            'IMDB_Rating': 'IMDB Rating',
            'Overview': 'Plot synopsis',
            'Meta_score': 'Metacritic rating if known',
            'Director': 'Director',
            'Star1': 'Actor 1',
            'Star2': 'Actor 2',
            'Star3': 'Actor 3',
            'Star4': 'Actor 4',
            'No_of_Votes': 'No. of IMDB votes which make the rating',
            'Gross': 'Gross film takings if known',
            'dvd_stock': 'DVD stock (currently unused field)',
            'bluray_stock': 'Blueray stock (currently unused field)',
            'available': 'Is the title available (currently unused field)',
        }
        self.fields['Poster_Link'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
