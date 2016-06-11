from django import forms


class NewRating(forms.Form):
    age = forms.IntegerField(label='Your age ')
    gender = forms.CharField(label='Your gender ', max_length=3)
    occupation = forms.CharField(label='Your occupation ', max_length=25)
    zip_code = forms.CharField(label='Your ZIP Code ', max_length=10)
    movie = forms.CharField(max_length=75)
    rating = forms.IntegerField()
