#!/bin/bash

source .venv/bin/activate
python3 thermolog/manage.py sync_weather >> thermolog/logs/sync_weather.log 2>&1