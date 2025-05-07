from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='test_index'),
    path('start/', views.start_test, name='start_test'),
    path('results/', views.test_results, name='test_results'),
]