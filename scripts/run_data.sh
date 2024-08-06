#!/bin/bash

cd "$HOME/system-monitoring-dashboard/scripts"
./populate_variable_data.sh &
./populate_DISK_data.sh &
