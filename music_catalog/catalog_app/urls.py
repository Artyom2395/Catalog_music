from django.urls import path

from . import views

urlpatterns = [
    path('artists/', views.ArtistListCreateView.as_view(), name='artist-list-create'),
    path('artists/<int:pk>/', views.ArtistDetailView.as_view(), name='artist-detail'),
   
    path('albums/', views.AlbumListCreateView.as_view(), name='album-list-create'),
    path('albums/<int:pk>/', views.AlbumDetailView.as_view(), name='album-detail'),
   
    path('songs/', views.SongListCreateView.as_view(), name='song-list-create'),
    path('songs/<int:pk>/', views.SongDetailView.as_view(), name='song-detail'),

    path('songalbums/', views.SongAlbumListCreateView.as_view(), name='songalbum-list-create'),
    path('songalbums/<int:pk>/', views.SongAlbumDetail.as_view(), name='songalbum-detail'),
]
