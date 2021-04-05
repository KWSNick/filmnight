from django.db import models

# Create your models here.


class film(models.Model):
    Poster_Link = models.URLField(max_length=2048, null=True, blank=True)
    Series_Title = models.CharField(max_length=254, null=True, blank=True)
    Released_Year = models.CharField(max_length=4, null=True, blank=True)
    Certificate = models.CharField(max_length=3, null=True, blank=True)
    Runtime = models.CharField(max_length=8, null=True, blank=True)
    Genre = models.CharField(max_length=20, null=True, blank=True)
    IMDB_Rating = models.DecimalField(max_digits=3,
                                      decimal_places=1,
                                      null=True,
                                      blank=True)
    Overview = models.TextField(null=True, blank=True)
    Meta_score = models.PositiveSmallIntegerField(null=True, blank=True)
    Director = models.CharField(max_length=50, null=True, blank=True)
    Star1 = models.CharField(max_length=50, null=True, blank=True)
    Star2 = models.CharField(max_length=50, null=True, blank=True)
    Star3 = models.CharField(max_length=50, null=True, blank=True)
    Star4 = models.CharField(max_length=50, null=True, blank=True)
    No_of_Votes = models.PositiveIntegerField(null=True, blank=True)
    Gross = models.CharField(max_length=50, null=True, blank=True)
    dvd_stock = models.IntegerField(null=True, blank=True)
    bluray_stock = models.IntegerField(null=True, blank=True)
    available = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.Series_Title
