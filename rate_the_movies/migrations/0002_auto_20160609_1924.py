# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 19:24
from __future__ import unicode_literals

from django.db import migrations


import csv


def rater_data(apps, schema_editor):
    Rater = apps.get_model("rate_the_movies", "Rater")

    with open("u.rater") as rater_file:
        fieldnames = ["age", "gender", "occupation", "zip_code"]
        raters = csv.DictReader(rater_file, delimiter="|", fieldnames=fieldnames)

        for row in raters:
            Rater.objects.create(
                age=int(row['age']),
                gender=row['gender'],
                occupation=row['occupation'],
                zip_code=row['zip_code']
            )
    raise Exception("rater passes")


def movie_data(apps, schema_editor):
    Movie = apps.get_model("rate_the_movies", "Movie")

    with open("u.movie", encoding="latin1") as movie_file:
        fieldnames = ["movie_title", "release_date", "video_release_date", "imdb_url",
                      "unknown", "action", "adventure", "animation", "children", "comedy", "crime",
                      "documentary", "drama", "fantasy", "film_noir", "horror", "musical", "mystery",
                      "romance", "scifi", "thriller", "war", "western"]
        movies = csv.DictReader(movie_file, delimiter="|", fieldnames=fieldnames)

        for row in movies:
            Movie.objects.create(
                movie_title=row["movie_title"], release_date=row["release_date"],
                video_release_date=row["video_release_date"], imdb_url=row["imdb_url"],
                unknown=int(row["unknown"]), action=int(row["action"]),
                adventure=int(row["adventure"]), animation=int(row["animation"]),
                children=int(row["children"]), comedy=int(row["comedy"]), crime=int(row["crime"]),
                documentary=int(row["documentary"]), drama=int(row["drama"]),
                fantasy=int(row["fantasy"]), film_noir=int(row["film_noir"]),
                horror=int(row["horror"]), musical=int(row["musical"]),
                mystery=int(row["mystery"]), romance=int(row["romance"]), scifi=int(row["scifi"]),
                thriller=int(row["thriller"]), war=int(row["war"]), western=int(row["western"])

            )

    raise Exception("movie passes")


def rating_data(apps, schema_editor):
    Rating = apps.get_model("rate_the_movies", "Movie")

    with open("u.rating") as rating_file:
        fieldnames = [""]
        pass


class Migration(migrations.Migration):

    dependencies = [
        ('rate_the_movies', '0001_initial'),
    ]

    operations = [
        # migrations.RunPython(rater_data)
        migrations.RunPython(movie_data)
        # migrations.RunPython(rating_data)
    ]
