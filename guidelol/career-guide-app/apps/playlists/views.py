from django.shortcuts import render
from .models import Playlist

def playlist_list(request):
    playlists = Playlist.objects.all()
    return render(request, 'playlists/index.html', {'playlists': playlists})

def playlist_detail(request, playlist_id):
    playlist = Playlist.objects.get(id=playlist_id)
    return render(request, 'playlists/detail.html', {'playlist': playlist})