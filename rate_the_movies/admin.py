from django.contrib import admin

# Register your models here.

from rate_the_movies.models import Rater, Movie, Rating, TopMovie

admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Rating)
admin.site.register(TopMovie)
