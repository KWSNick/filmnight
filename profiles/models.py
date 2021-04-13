from django.db import models
from django.contrib.auth.models import User
from films.models import film
from django_countries.fields import CountryField

# Create your models here.


class users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    delivery_add1 = models.CharField(max_length=80, null=False, blank=False)
    delivery_add2 = models.CharField(max_length=80, null=True, blank=True)
    delivery_town = models.CharField(max_length=40, null=False, blank=False)
    delivery_county = models.CharField(max_length=80, null=True, blank=True)
    delivery_postcode = models.CharField(max_length=40, null=True, blank=True)
    delivery_country = CountryField(
        blank_label='Country_*', null=False, blank=False)
    billing_add1 = models.CharField(max_length=80, null=False, blank=False)
    billing_add2 = models.CharField(max_length=80, null=True, blank=True)
    billing_town = models.CharField(max_length=40, null=False, blank=False)
    billing_county = models.CharField(max_length=80, null=True, blank=True)
    billing_postcode = models.CharField(max_length=40, null=True, blank=True)
    billing_country = CountryField(
        blank_label='Country_*', null=False, blank=False)
    purchased_titles = models.ManyToManyField(film)

    def __str__(self):
        return self.user.username
