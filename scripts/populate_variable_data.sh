#!/bin/bash

./collect_disk_space.sh &
for i in {1..60}; do
  ./collect_cpu_usage.sh &
  ./collect_memory_usage.sh &
  ./collect_network_activity.sh &
  sleep 60
done