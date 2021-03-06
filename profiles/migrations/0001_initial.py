# Generated by Django 3.1.7 on 2021-04-21 22:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('films', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('delivery_add1', models.CharField(max_length=80)),
                ('delivery_add2', models.CharField(blank=True, max_length=80, null=True)),
                ('delivery_town', models.CharField(max_length=40)),
                ('delivery_county', models.CharField(blank=True, max_length=80, null=True)),
                ('delivery_postcode', models.CharField(blank=True, max_length=40, null=True)),
                ('delivery_country', django_countries.fields.CountryField(max_length=2)),
                ('billing_add1', models.CharField(max_length=80)),
                ('billing_add2', models.CharField(blank=True, max_length=80, null=True)),
                ('billing_town', models.CharField(max_length=40)),
                ('billing_county', models.CharField(blank=True, max_length=80, null=True)),
                ('billing_postcode', models.CharField(blank=True, max_length=40, null=True)),
                ('billing_country', django_countries.fields.CountryField(max_length=2)),
                ('purchased_titles', models.ManyToManyField(to='films.film')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
