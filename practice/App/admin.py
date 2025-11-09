from django.contrib import admin
from .models import IMDBRating, Actor, Director, Movie, Album, Song

admin.site.register(IMDBRating)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Movie)
admin.site.register(Album)
admin.site.register(Song)
