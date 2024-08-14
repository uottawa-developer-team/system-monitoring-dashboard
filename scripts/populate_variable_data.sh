#!/bin/bash

process_ids=$(ps -e | grep "populate" | awk '{print $1}' | sort -n) # extracts PIDs for the populate script

if [ $(echo "$process_ids" | wc -l) -gt 2 ]; then # checks if the process_ids are greater than 1
  oldest_process_id=$(echo "$process_ids" | head -n 1)
  kill -9 $oldest_process_id &> /dev/null
fi

./collect_disk_space.sh
for i in {1..60}; do
  ./collect_cpu_usage.sh &
  ./collect_memory_usage.sh &
  ./collect_network_activity.sh &
  sleep 60
done