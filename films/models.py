from django.db import models

# Create your models here.


class film(models.Model):
    poster_link = models.URLField(max_length=2048, null=True, blank=True)
    series_title = models.CharField(max_length=254, null=True, blank=True)
    released_year = models.CharField(max_length=4, null=True, blank=True)
    certificate = models.CharField(max_length=3, null=True, blank=True)
    runtime = models.CharField(max_length=8, null=True, blank=True)
    genre = models.CharField(max_length=20, null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=3,
                                      decimal_places=1,
                                      null=True,
                                      blank=True)
    overview = models.TextField(null=True, blank=True)
    meta_score = models.PositiveSmallIntegerField(null=True, blank=True)
    director = models.CharField(max_length=50, null=True, blank=True)
    star1 = models.CharField(max_length=50, null=True, blank=True)
    star2 = models.CharField(max_length=50, null=True, blank=True)
    star3 = models.CharField(max_length=50, null=True, blank=True)
    star4 = models.CharField(max_length=50, null=True, blank=True)
    no_of_votes = models.PositiveIntegerField(null=True, blank=True)
    gross = models.CharField(max_length=50, null=True, blank=True)
    dvd_stock = models.IntegerField(null=True, blank=True)
    bluray_stock = models.IntegerField(null=True, blank=True)
    available = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return self.series_title
