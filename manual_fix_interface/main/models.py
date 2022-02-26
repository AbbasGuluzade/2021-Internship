from django.db import models
from .YYY import elements
import os

# Create your models here.

class Polygon(models.Model):
    polygon_id = models.IntegerField()
    coordinates = models.CharField(max_length=200)
    polygon_class = models.IntegerField()

class Match(models.Model):
    text_polygon_id = models.IntegerField(primary_key=True)
    text = models.CharField(max_length=30)


def BulkInsert():
    
    print("slm nbr")

    counter = 1

    polygon_list = []

    for element in elements:
        polygon_list.append(Polygon(polygon_id = counter, coordinates = str(element[:-1]), polygon_class = element[-1]))
        counter = counter + 1

    Polygon.objects.bulk_create(polygon_list)