# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 18:23
from __future__ import unicode_literals

from django.db import migrations

from django.db.models import Avg, Count


def top_movies(apps, schema_editor):
    Movie = apps.get_model("rate_the_movies", "Movie")
    Rating = apps.get_model("rate_the_movies", "Rating")
    TopMovie = apps.get_model("rate_the_movies", "TopMovie")

    movies = Movie.objects.all()
    for movie_object in movies:
        temp_id = movie_object.id
        temp_average = Rating.objects.filter(movie=temp_id).aggregate(Avg('rating'))
        average = list(temp_average.values())
        final_average = average[0]
        total = Rating.objects.filter(movie=temp_id).count()
        TopMovie.objects.create(
            movie=movie_object,
            avg_rating=final_average,
            times_rated=total
        )

    # raise Exception("ALL IS WELL ----- ALL IS WELL ----- ALL IS WELL")


class Migration(migrations.Migration):

    dependencies = [
        ('rate_the_movies', '0005_auto_20160611_1823'),
    ]

    operations = [
        migrations.RunPython(top_movies)
    ]