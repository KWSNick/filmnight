# Generated by Django 3.1.7 on 2021-04-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='Poster',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
