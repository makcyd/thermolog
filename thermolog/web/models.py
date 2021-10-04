from django.db import models


class Thermometer(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")

    thing_name = models.CharField(max_length=26, verbose_name="name", unique=True)
    thing_nick_name = models.CharField(max_length=1024, verbose_name="friendly name")
    sub_type = models.CharField(max_length=10, verbose_name="type code")

    def __str__(self):
        return "{} ({})".format(self.thing_nick_name, self.thing_name)


class ThermoRecord(models.Model):

    CHOICES = (
        ("success", "success"),
        ("error", "error")
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")

    thermometer = models.ForeignKey(Thermometer, on_delete=models.PROTECT)

    sync_status = models.CharField(max_length=256, verbose_name="sync status", choices=CHOICES)

    connected = models.BooleanField(verbose_name="is connected")
    working_status = models.CharField(max_length=256, verbose_name="working status", null=True)
    air_tem = models.IntegerField(null=True, verbose_name="air temperature")
    floor_tem = models.IntegerField(null=True, verbose_name="floor temperature")

    def __str__(self):
        return "{} - {:%Y-%m-%d %H:%M}".format(self.thermometer.thing_nick_name, self.created_at)

class WeatherRecord(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")

    # some info from WeatherAPI: https://www.weatherapi.com/docs/
    location_name = models.CharField(max_length=256, verbose_name="location_name")
    location = models.JSONField(null=True, verbose_name="location")
    last_updated = models.DateTimeField(null=True, verbose_name="last_updated")
    temp_c = models.FloatField(null=True, verbose_name="temperature_celcius")
    feelslike_c = models.FloatField(null=True, verbose_name="feelslike_celcius")
    is_day = models.BooleanField(null=True, verbose_name="is_day")
    condition = models.JSONField(null=True, verbose_name="condition")
    wind_kph = models.FloatField(null=True, verbose_name="wind_speed_km/h")
    wind_degree = models.FloatField(null=True, verbose_name="wind_degree")
    wind_dir = models.CharField(max_length=10, null=True, verbose_name="wind_direction")
    pressure_mb = models.FloatField(null=True, verbose_name="pressure_mb")
    precip_mm = models.FloatField(null=True, verbose_name="precip_mm")
    humidity = models.IntegerField(null=True, verbose_name="humidity")
    cloud = models.IntegerField(null=True, verbose_name="cloud")
    vis_km = models.FloatField(null=True, verbose_name="visibility_km")
    uv = models.FloatField(null=True, verbose_name="ultraviolet index")
    gust_km = models.FloatField(null=True, verbose_name="wind gust")

    def __str__(self):
        return "{}@{:%Y-%m-%d %H:%M}: {}".format(self.location_name, self.last_updated, self.temp_c)

    class Meta:
        unique_together = ["location_name", "last_updated"]
