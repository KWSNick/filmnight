# Generated by Django 3.1.7 on 2021-04-11 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='price_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost_name', models.CharField(max_length=20)),
                ('cost_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]