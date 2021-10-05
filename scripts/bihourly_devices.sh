#!/bin/bash
cd /opt/thermolog
source .venv/bin/activate
python3 thermolog/manage.py sync_thermometer >> thermolog/logs/sync_thermometer.log 2>&1