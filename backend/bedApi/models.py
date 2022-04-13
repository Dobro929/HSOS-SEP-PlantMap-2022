import uuid

from django.db import models

# GEOLOCATION
class Geolocation(models.Model):
    coordinateSystem = models.CharField(max_length=100)
    ellipsoid = models.CharField(max_length=100)
    latitude =  models.FloatField()
    longitude = models.FloatField()

    # ToString
    def __str__(self):
        return self.latitude


# BED
class Bed(models.Model):
    uuid = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=100)
    geolocation = models.OneToOneField(
        Geolocation,
        on_delete=models.CASCADE,
        #primary_key=True,
    )

    # ToString
    def __str__(self):
        return self.name


# GEOMETRIE
class Geometrie(models.Model):
    name = models.CharField(max_length=100)
    uuid = models.CharField(primary_key= True, max_length=100)
    type =  models.CharField(max_length=100)
    frameId = models.CharField(max_length=100)
    stamp = models.CharField(max_length=100)
    bed = models.ForeignKey(Bed, on_delete=models.CASCADE)

    # ToString
    def __str__(self):
        return self.name
