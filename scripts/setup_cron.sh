#!/bin/bash

# Get the absolute path of the populate_variable_data.sh script
SCRIPT_PATH=$(realpath "$(dirname "$0")/populate_variable_data.sh")

# Check if the script file exists
if [[ ! -f "$SCRIPT_PATH" ]]; then
    echo "SYSTEM MONITORING DASHBOARD ERROR: Script $SCRIPT_PATH does not exist."
    exit 1
fi

# Define the cron job
CRON_JOB="0 * * * * \"$SCRIPT_PATH\""

# Check if the cron job already exists
EXISTING_CRON=$(crontab -l 2>/dev/null | grep -F "$SCRIPT_PATH")

if [[ -n "$EXISTING_CRON" ]]; then
    echo "SYSTEM MONITORING DASHBOARD: Cron job already exists."
else
    # Append the cron job if it doesn't exist
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
    if [[ $? -eq 0 ]]; then
        echo "SYSTEM MONITORING DASHBOARD: Cron job added successfully."
    else
        echo "SYSTEM MONITORING DASHBOARD ERROR: Failed to add cron job."
    fi
fi
