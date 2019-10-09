from django.contrib import admin
from django.contrib.postgres import fields
from django_json_widget.widgets import JSONEditorWidget
from django.contrib.gis.admin import OSMGeoAdmin
from . models import *

# Register your models here.


@admin.register(WGProject)
class WGProjectAdmin(OSMGeoAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(WGPoint)
class WGPointAdmin(OSMGeoAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(WGMultiPoint)
class WGPointAdmin(OSMGeoAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(WGLineString)
class WGPointAdmin(OSMGeoAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(WGMultiLineString)
class WGPointAdmin(OSMGeoAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(WGPolygon)
class WGPointAdmin(OSMGeoAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

@admin.register(WGMultiPolygon)
class WGPointAdmin(OSMGeoAdmin):
    formfield_overrides = {
        fields.JSONField: {'widget': JSONEditorWidget},
    }

