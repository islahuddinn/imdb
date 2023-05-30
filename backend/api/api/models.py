from django.db import models

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    original_title = models.CharField(max_length=255)
    original_language = models.CharField(max_length=2)
    backdrop_path = models.CharField(max_length=255)
    overview = models.TextField()
    popularity = models.FloatField()
    release_date = models.DateField()
    poster_path = models.CharField(max_length=255)
    vote_count = models.IntegerField()

    def __str__(self):
        return self.title
