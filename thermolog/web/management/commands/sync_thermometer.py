import logging

from django.core.management import BaseCommand
from django.conf import settings
from weback_unofficial.client import WebackApi
from ...models import Thermometer, ThermoRecord

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    help = "Sync thermometer data"

    def handle(self, *args, **options):
        devices = Thermometer.objects.all()

        c = WebackApi(settings.WEBACK["username"], settings.WEBACK["password"])
        logger.debug("WebackClient: {}".format(c))
        s = c.get_session()
        logger.debug("Session: {}".format(s))

        for device in devices:
            status = c.get_device_shadow(device.thing_name)

            if status:
                tr = ThermoRecord.objects.create(thermometer=device, sync_status="success",
                                                 connected=True if status.get("connected") == 'true' else False)
                tr.working_status = status.get("working_status")
                tr.air_tem = status.get("air_tem")
                tr.floor_tem =status.get("floor_tem")
                tr.save()
            else:
                tr = ThermoRecord.objects.create(thermometer=device, sync_status="error", connected=False)
                tr.save()