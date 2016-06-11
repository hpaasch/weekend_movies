from django.db import models


class Rater(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=3)
    occupation = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.id

    # def average_score(self):
        # deliver each rater's avg rating


    #     pass

    # def not_yet_seen(self):
        # top-rated movies not seen yet for each rater

    #     pass


class Movie(models.Model):
    movie_title = models.CharField(max_length=75)
    release_date = models.CharField(max_length=20)
    video_release_date = models.CharField(max_length=20, default="")
    imdb_url = models.CharField(max_length=300)
    unknown = models.IntegerField()
    action = models.IntegerField()
    adventure = models.IntegerField()
    animation = models.IntegerField()
    children = models.IntegerField()
    comedy = models.IntegerField()
    crime = models.IntegerField()
    documentary = models.IntegerField()
    drama = models.IntegerField()
    fantasy = models.IntegerField()
    film_noir = models.IntegerField()
    horror = models.IntegerField()
    musical = models.IntegerField()
    mystery = models.IntegerField()
    romance = models.IntegerField()
    scifi = models.IntegerField()
    thriller = models.IntegerField()
    war = models.IntegerField()
    western = models.IntegerField()

    def __str__(self):
        return self.movie_title



    # class Meta:
    #      ordering = # order by the average_rating?
#
#
    #     pass

    def nearest_neighbor(self, rater_a, rater_b):
        rater_a_list = ["A", "B", "C", "D"]
        rater_b_list = ["B", "D", "E", "F"]
        seta = set(rater_a_list)
        setb = set(rater_b_list)
        shared = seta.intersection(setb)
        print(shared)
        pass


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.IntegerField()

    # def __str__(self):
    #     return self.movie


