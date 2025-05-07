from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='guidance_index'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    path('test/<int:test_id>/', views.test_detail, name='test_detail'),
    path('playlists/', views.playlist_list, name='playlist_list'),
    path('playlists/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
]