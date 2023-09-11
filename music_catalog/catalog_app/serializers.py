from rest_framework import serializers

from .models import Artist, Album, Song, SongAlbum


class SongAlbumSerializer(serializers.ModelSerializer):
    album = serializers.PrimaryKeyRelatedField(
        queryset=Album.objects.all(),
        write_only=True
    )
    
    class Meta:
        model = SongAlbum
        fields = ('id', 'song','album', 'track_number')

class SongSerializer(serializers.ModelSerializer):
    albums = SongAlbumSerializer(many=True)
   
    class Meta:
        model = Song
        fields = ('title', 'track_number', 'albums')

    def create(self, validated_data):
        albums_data = validated_data.pop('albums')
        
        song = Song.objects.create(**validated_data)
        for album_data in albums_data:
            SongAlbum.objects.create(song=song, **album_data)
        return song
   
class AlbumSerializer(serializers.ModelSerializer):
    songs = SongAlbumSerializer(many=True, read_only=True)   
    artist_id = serializers.PrimaryKeyRelatedField(
        queryset=Artist.objects.all(),
        source='artist'
    )
  
    class Meta:
        model = Album
        fields = ('title', 'songs','release_year', 'artist_id')    

class ArtistSerializer(serializers.ModelSerializer):
    albums = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('name', 'albums')