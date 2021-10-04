import logging

from django.core.management import BaseCommand
from django.conf import settings
from weback_unofficial.client import WebackApi
from ...models import Thermometer

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "Synchronizes devices"

    def handle(self, *args, **options):
        c = WebackApi(settings.WEBACK["username"], settings.WEBACK["password"])
        logger.debug("WebackClient: {}".format(c))
        s = c.get_session()
        logger.debug("Session: {}".format(s))

        for device in c.device_list():
            logger.debug("Device: {}".format(device))
            d, created = Thermometer.objects.get_or_create(thing_name=device.get("Thing_Name"))
            if created:
                d.thing_name = device.get("Thing_Name")
                d.thing_nick_name = device.get("Thing_Nick_Name")
                d.sub_type = device.get("Sub_type")
                d.save()