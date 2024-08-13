#!/bin/bash

SCRIPT_PATH="./populate_variable_data.sh"
CRON_JOB="0 * * * * $SCRIPT_PATH"

crontab -l 2>/dev/null | grep -v -F "$CRON_JOB" | crontab -