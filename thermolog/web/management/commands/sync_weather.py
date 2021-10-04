import logging

from django.core.management import BaseCommand
from django.conf import settings
from ...weatherapi import *
from ...models import WeatherRecord

logger = logging.getLogger(__name__)

class Command(BaseCommand):

    help = "Sync weather data"

    def handle(self, *args, **options):
        w = get_current()

        if w is not None:
            current = w.get('current')
            logger.debug(current)

            wr, created = WeatherRecord.objects.get_or_create(location_name=w.get('location').get('name'),
                                                              last_updated=current.get('last_updated'))

            if created:
                wr.temp_c = current.get('temp_c')
                wr.feelslike_c = current.get('feelslike_c')
                wr.last_updated = current.get('last_updated')
                wr.is_day = current.get('is_day')
                wr.condition = current.get('condition')
                wr.wind_kph = current.get('wind_kph')
                wr.wind_degree = current.get('wind_degree')
                wr.wind_dir = current.get('wind_dir')
                wr.pressure_mb = current.get('pressure_mb')
                wr.precip_mm = current.get('precip_mm')
                wr.humidity = current.get('humidity')
                wr.cloud = current.get('cloud')
                wr.vis_km = current.get('vis_km')
                wr.uv = current.get('uv')
                wr.gust_km = current.get('gust_km')
                wr.save()
