from django.shortcuts import render

# Create your views here.
from rate_the_movies.models import Rating, Rater, Movie


def top_movies(request):
    context = {
        "movies": list(Movie.objects.all()),

    }
    return render(request, "movie_list.html", context)
    # deliver each movie's average rating


def one_rater(request, rater):  # add arg rater
    context = {

            "rater": list(Rater.objects.all())
        }
    return render(request, "one_rater.html", context)
        # deliver each movie's average rating


def one_movie(request, movie_title):
    context = {
        "movie": Movie.objects.get(id=movie_title)
    }
    return render(request, "one_movie.html", context)


def homepage(request):
    return render(request, "homepage.html")


