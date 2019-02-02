from django.db import models

class Movie(models.Model):
    artist = models.CharField(max_length=250)#text
    movie_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    #post link to use images online
    movie_logo = models.CharField(max_length=200)

    def __str__(self): #string representation of object
        return self.movie_title + ' - ' + self.artist

class themeSong(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    file_type = models.CharField(max_length = 10)
    song_title = models.CharField(max_length = 250)
    is_favorite = models.BooleanField(default=False)


    def __str__(self):
        return self.song_title
