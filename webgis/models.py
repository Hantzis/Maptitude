from django.contrib.gis.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User

# Create your models here.

class WGCell(models.Model):
    cell_geom = models.PolygonField(srid=3857)
    cell_user = models.ForeignKey(User, on_delete=models.PROTECT, )


class WGProject(models.Model):
    project_name = models.CharField(max_length=255)
    project_owner = models.ForeignKey(User, on_delete=models.PROTECT, related_name='owner_project')
    project_users = models.ManyToManyField(User, related_name='users_project')
    project_cellsize = models.PositiveIntegerField(default=1000)
    project_cells = models.ManyToManyField(WGCell, blank=True, null=True)
    project_geom = models.PolygonField(srid=3857)
    project_sridutm = models.PositiveIntegerField(default=32613)

    def __str__(self):
        return f'{self.project_name}'


class WGPoint(models.Model):
    point_geom = models.PointField(srid=3857)
    point_data = JSONField(blank=True, null=True)

class WGMultiPoint(models.Model):
    multipoint_geom = models.MultiPointField(srid=3857)
    multipoint_data = JSONField(blank=True, null=True)

class WGLineString(models.Model):
    linestring_geom = models.LineStringField(srid=3857)
    linestring_data = JSONField(blank=True, null=True)

class WGMultiLineString(models.Model):
    multilinestring_geom = models.MultiLineStringField(srid=3857)
    multilinestring_data = JSONField(blank=True, null=True)

class WGPolygon(models.Model):
    polygon_geom = models.MultiPolygonField(srid=3857)
    polygon_data = JSONField(blank=True, null=True)

class WGMultiPolygon(models.Model):
    multipolygon_geom = models.MultiPolygonField(srid=3857)
    multipolygon_data = JSONField(blank=True, null=True)
