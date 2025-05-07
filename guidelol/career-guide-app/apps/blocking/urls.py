from django.urls import path
from . import views

urlpatterns = [
    # Distraction Blocking URLs
    path('', views.index, name='blocking_index'),
    path('settings/', views.settings, name='blocking_settings'),

    # Profile URLs
    path('profile/', views.profile_overview, name='profile_overview'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),  # POST handler
]
