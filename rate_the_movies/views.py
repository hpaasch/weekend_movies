from django.shortcuts import render

from django.http import HttpResponseRedirect

from rate_the_movies.forms import NewRating

from rate_the_movies.models import Rating, Rater, Movie, TopMovie
from django.db.models import Avg


def top_movies(request):
    context = {
        "top_movies": TopMovie.objects.filter(times_rated__gte=100).order_by('-avg_rating')[:20]
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


def get_rating(request):
    if request.method == 'POST':
        form = NewRating(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/Thanks!/')
    else:
        form = NewRating()
    return render(request, 'add_rating.html', {'form': form})


def homepage(request):
    return render(request, "homepage.html")


