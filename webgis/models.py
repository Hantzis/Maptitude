from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User

# Create your models here.

class WGProject(models.Model):
    project_name = models.CharField(max_length=255)
    project_owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owner_project')
    project_users = models.ManyToManyField(User, related_name='users_project')
    project_cellsize = models.PositiveIntegerField(default=1000)
    project_geom = models.PolygonField()

    def __str__(self):
        return f'{self.project_name}'


class WGPoint(models.Model):
    point_geom = models.PointField()
    point_data = JSONField(blank=True, null=True)

class WGMultiPoint(models.Model):
    multipoint_geom = models.MultiPointField()
    multipoint_data = JSONField(blank=True, null=True)

class WGLineString(models.Model):
    linestring_geom = models.LineStringField()
    linestring_data = JSONField(blank=True, null=True)

class WGMultiLineString(models.Model):
    multilinestring_geom = models.MultiLineStringField()
    multilinestring_data = JSONField(blank=True, null=True)

class WGPolygon(models.Model):
    polygon_geom = models.MultiPolygonField()
    polygon_data = JSONField(blank=True, null=True)

class WGMultiPolygon(models.Model):
    multipolygon_geom = models.MultiPolygonField()
    multipolygon_data = JSONField(blank=True, null=True)
