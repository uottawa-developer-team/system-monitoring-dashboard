#!/bin/bash

# Ensure that the script path is absolute
SCRIPT_PATH="$(realpath ./.processes/scripts/smd_process.sh)"
CRON_JOB="0 * * * * $SCRIPT_PATH"

# Remove the cron job if it exists
if crontab -l 2>/dev/null | grep -F "$CRON_JOB" >/dev/null; then
    crontab -l 2>/dev/null | grep -v -F "$CRON_JOB" | crontab -
    echo "SYSTEM MONITORING DASHBOARD: Cron job removed successfully."
else
    echo "SYSTEM MONITORING DASHBOARD: No matching cron job found."
fi
