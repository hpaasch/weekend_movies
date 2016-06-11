from django import forms
from rate_the_movies.models import Rating, Rater, Movie


class NewRating(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ('movie', 'rating', 'timestamp', 'rater')



