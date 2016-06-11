# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 16:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rate_the_movies', '0003_topmovies'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_rating', models.IntegerField()),
                ('times_rated', models.IntegerField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rate_the_movies.Movie')),
            ],
        ),
        migrations.RemoveField(
            model_name='topmovies',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='topmovies',
            name='rater',
        ),
        migrations.RemoveField(
            model_name='topmovies',
            name='rating',
        ),
        migrations.DeleteModel(
            name='TopMovies',
        ),
    ]
