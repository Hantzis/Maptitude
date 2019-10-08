from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class WGPoint(models.Model):
    geom = models.PointField()
    data = JSONField()

