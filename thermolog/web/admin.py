from django.contrib import admin
from .models import *


@admin.register(Thermometer)
class ThermometerAdmin(admin.ModelAdmin):
    readonly_fields = ["thing_name", "thing_nick_name", "sub_type", "created_at", "updated_at"]
    list_display = ["thing_name", "thing_nick_name"]


@admin.register(ThermoRecord)
class ThermoRecordAdmin(admin.ModelAdmin):
    readonly_fields = []
    list_display = ["created_at", "thermometer", "air_tem", "floor_tem", "sync_status", "connected"]

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
            [field.name for field in obj._meta.fields] + \
            [field.name for field in obj._meta.many_to_many]


@admin.register(WeatherRecord)
class WeatherRecordAdmin(admin.ModelAdmin):
    readonly_fields = []
    list_display = ["created_at", "temp_c", "feelslike_c"]

    def get_readonly_fields(self, request, obj=None):
        return list(self.readonly_fields) + \
               [field.name for field in obj._meta.fields] + \
               [field.name for field in obj._meta.many_to_many]