# Generated by Django 2.1.5 on 2019-01-14 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_movie_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='is_favorite',
        ),
        migrations.AddField(
            model_name='themesong',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]
