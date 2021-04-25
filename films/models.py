from django.db import models

# Create your models here.


class film(models.Model):
    Poster = models.ImageField(null=True, blank=True) # noqa
    Poster_Link = models.URLField(max_length=2048, null=True, blank=True) # noqa
    Series_Title = models.CharField(max_length=254, null=True, blank=True) # noqa
    Released_Year = models.CharField(max_length=4, null=True, blank=True) # noqa
    Certificate = models.CharField(max_length=8, null=True, blank=True) # noqa
    Runtime = models.CharField(max_length=8, null=True, blank=True) # noqa
    Genre = models.CharField(max_length=100, null=True, blank=True) # noqa
    IMDB_Rating = models.DecimalField(max_digits=3,
                                      decimal_places=1,
                                      null=True,
                                      blank=True) # noqa
    Overview = models.TextField(null=True, blank=True) # noqa
    Meta_score = models.PositiveSmallIntegerField(null=True, blank=True) # noqa
    Director = models.CharField(max_length=50, null=True, blank=True) # noqa
    Star1 = models.CharField(max_length=50, null=True, blank=True) # noqa
    Star2 = models.CharField(max_length=50, null=True, blank=True) # noqa
    Star3 = models.CharField(max_length=50, null=True, blank=True) # noqa
    Star4 = models.CharField(max_length=50, null=True, blank=True) # noqa
    No_of_Votes = models.PositiveIntegerField(null=True, blank=True) # noqa
    Gross = models.CharField(max_length=50, null=True, blank=True) # noqa
    dvd_stock = models.IntegerField(null=True, blank=True)
    bluray_stock = models.IntegerField(null=True, blank=True)
    available = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.Series_Title
