from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=200)

    def  __str__(self) -> str:
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    release_year = models.PositiveIntegerField()

    def  __str__(self) -> str:
        return self.title

class Song(models.Model):
    albums = models.ManyToManyField(Album, related_name='songs', through='SongAlbum')
    title = models.CharField(max_length=200)
    track_number = models.PositiveIntegerField()
    
    def  __str__(self) -> str:
        return self.title
    
class SongAlbum(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    track_number = models.PositiveIntegerField(default=1)
