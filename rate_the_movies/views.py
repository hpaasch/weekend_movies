from django.shortcuts import render

from rate_the_movies.models import Rating, Rater, Movie
from django.db.models import Avg, Count

def top_movies(request):
    context = {
        "top_movies": (Rating.objects.annotate(xxx=Count('yyy').order_by('-xxx')[:20]),
        # Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')[:5]

    }
    return render(request, "movie_list.html", context)


def one_rater(request, rater_id):
    context = {
            "rater": Rater.objects.get(id=rater_id),
            "id": rater_id,
            "ratings": Rating.objects.filter(rater=rater_id),
            "total": Rating.objects.filter(rater=rater_id).count(),
            "average": Rating.objects.filter(rater=rater_id).aggregate(Avg('rating')),
        }
    return render(request, "one_rater.html", context)


def one_movie(request, movie_id):
    context = {
        "movie": Movie.objects.get(id=movie_id),
        "average": Rating.objects.filter(movie=movie_id).aggregate(Avg('rating')),
        "total": Rating.objects.filter(movie=movie_id).count(),
        "ratings": Rating.objects.filter(movie=movie_id)
    }
    return render(request, "one_movie.html", context)


def homepage(request):
    return render(request, "homepage.html")


