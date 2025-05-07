from django.urls import path
from . import views

urlpatterns = [
    path('', views.playlist_list, name='playlist_list'),
    path('<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
    path('create/', views.playlist_create, name='playlist_create'),
    path('edit/<int:playlist_id>/', views.playlist_edit, name='playlist_edit'),
]