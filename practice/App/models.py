from django.db import models


class IMDBRating(models.Model):
    score = models.CharField(max_length=5)    
    rating_count = models.IntegerField()       

    def __str__(self):
        return f"{self.score} ({self.rating_count} ratings)"


class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()

    imdb_rating = models.OneToOneField(IMDBRating, on_delete=models.CASCADE, related_name="movie")

    actors = models.ManyToManyField(Actor, related_name="movies")

    director = models.OneToOneField(Director, on_delete=models.CASCADE, related_name="movies")

    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()

    def __str__(self):
        return self.title


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs")
    duration = models.CharField(max_length=10)  

    def __str__(self):
        return f"{self.title} ({self.album.title})"
