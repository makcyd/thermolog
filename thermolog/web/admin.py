from django.contrib import admin
from django.http import HttpResponse
from .models import *

import csv

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        writer.writerow(field_names)

        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export selected"


@admin.register(Thermometer)
class ThermometerAdmin(admin.ModelAdmin, ExportCsvMixin):
    readonly_fields = ["thing_name", "thing_nick_name", "sub_type", "created_at", "updated_at"]
    list_display = ["thing_name", "thing_nick_name"]
    actions = ["export_as_csv"]


@admin.register(ThermoRecord)
class ThermoRecordAdmin(admin.ModelAdmin, ExportCsvMixin):
    readonly_fields = ["get_air_tem", "get_floor_tem"]
    list_display = ["created_at", "thermometer", "get_air_tem", "get_floor_tem", "sync_status", "connected"]
    actions = ["export_as_csv"]

    def get_air_tem(self, obj):
        return "{:.1f} °C".format(obj.air_tem/10)

    def get_floor_tem(self, obj):
        return "{:.1f} °C".format(obj.floor_tem/10)

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
            [field.name for field in obj._meta.fields] + \
            [field.name for field in obj._meta.many_to_many]


@admin.register(WeatherRecord)
class WeatherRecordAdmin(admin.ModelAdmin, ExportCsvMixin):
    readonly_fields = []
    list_display = ["created_at", "temp_c", "feelslike_c"]
    actions = ["export_as_csv"]

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]