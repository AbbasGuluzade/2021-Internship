from os import name
from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('databaseLoad', views.databaseLoad, name='databaseLoad'),
    path('change_polygon_class', views.change_polygon_class, name='change_polygon_class'),
    path('pull_polygons_from_database', views.pull_polygons_from_database, name='pull_polygons_from_database'),
    path('get_match', views.get_match, name='get_match'),
    path('download_match', views.download_match, name='download_match')
    ]
