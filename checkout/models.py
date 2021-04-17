import uuid

from django.db import models
from django_countries.fields import CountryField
from profiles.models import users

# Create your models here.


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user = models.ForeignKey(
        users, on_delete=models.SET_NULL, null=True, blank=True)
    first_name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=25, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    delivery_add1 = models.CharField(max_length=80, null=False, blank=False)
    delivery_add2 = models.CharField(max_length=80, null=True, blank=True)
    delivery_town = models.CharField(max_length=40, null=False, blank=False)
    delivery_county = models.CharField(max_length=80, null=True, blank=True)
    delivery_postcode = models.CharField(max_length=40, null=True, blank=True)
    delivery_country = CountryField(
        blank_label='Country*', null=False, blank=False)
    billing_add1 = models.CharField(
        max_length=80, null=False, blank=False, default='')
    billing_add2 = models.CharField(max_length=80, null=True, blank=True)
    billing_town = models.CharField(
        max_length=40, null=False, blank=False, default='')
    billing_county = models.CharField(max_length=80, null=True, blank=True)
    billing_postcode = models.CharField(max_length=40, null=True, blank=True)
    billing_country = CountryField(
        blank_label='Country*', null=False, blank=False, default='GB')
    date = models.DateTimeField(auto_now_add=True)
    basket = models.TextField(null=False, blank=False, default='')
    delivery_charge = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0)
    order_charge = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    total_charge = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def order_no(self):
        """Generates a random unique order no
        based on CI Boutique Ado project"""
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """Override the save method so the order
        number can be set, if it doesn't exist"""
        if not self.order_number:
            self.order_number = self.order_no()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number
