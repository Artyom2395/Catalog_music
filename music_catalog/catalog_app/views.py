from rest_framework import generics, status

from .models import Artist, Album, Song, SongAlbum
from .serializers import ArtistSerializer, AlbumSerializer, SongSerializer, SongAlbumSerializer

# Представление для списка и создания исполнителей
class ArtistListCreateView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

# Представление для деталей и обновления/удаления исполнителей
class ArtistDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class AlbumListCreateView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class AlbumDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class SongListCreateView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class SongAlbumListCreateView(generics.ListCreateAPIView):
    queryset = SongAlbum.objects.all()
    serializer_class = SongAlbumSerializer

class SongAlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SongAlbum.objects.all()
    serializer_class = SongAlbumSerializer