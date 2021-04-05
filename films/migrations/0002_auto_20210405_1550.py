# Generated by Django 3.1.7 on 2021-04-05 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='certificate',
            new_name='Certificate',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='director',
            new_name='Director',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='genre',
            new_name='Genre',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='gross',
            new_name='Gross',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='imdb_rating',
            new_name='IMDB_Rating',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='meta_score',
            new_name='Meta_score',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='no_of_votes',
            new_name='No_of_Votes',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='overview',
            new_name='Overview',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='poster_link',
            new_name='Poster_Link',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='released_year',
            new_name='Released_Year',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='runtime',
            new_name='Runtime',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='series_title',
            new_name='Series_Title',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='star1',
            new_name='Star1',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='star2',
            new_name='Star2',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='star3',
            new_name='Star3',
        ),
        migrations.RenameField(
            model_name='film',
            old_name='star4',
            new_name='Star4',
        ),
    ]
