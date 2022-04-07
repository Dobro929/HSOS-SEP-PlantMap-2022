import uuid

from django.db import models


# BED
class Bed(models.Model):
    uuid = models.UUIDField()
    name = models.CharField(max_length=100)

    # ToString
    def __str__(self):
        return self.name
