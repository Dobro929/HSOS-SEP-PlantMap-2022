from django.db import models
import uuid
# BED
class Bed(models.Model):
    uuid = models.UUIDField()
    name = models.CharField(max_length=100)

    # ToString
    def __str__(self):
        return self.name