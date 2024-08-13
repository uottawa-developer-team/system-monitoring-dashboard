#!/bin/bash

SCRIPT_PATH="./populate_variable_data.sh"
chmod +x "$SCRIPT_PATH" #ensure the script is executable

#check if cron job already exists
if crontab -l 2>/dev/null | grep -F "$CRON_JOB"; then
    echo "SYSTEM MONITORING DASHBOARD ERROR: Cron job already exists" #dont make a new one
else
    #append the cron job if it doesn't exist
    (crontab -l 2>/dev/null; echo "$CRON_JOB") | crontab -
fi