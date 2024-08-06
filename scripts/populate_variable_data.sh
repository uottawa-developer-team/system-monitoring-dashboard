#!/bin/bash

while true; do
  ./collect_cpu_usage.sh &
  ./collect_memory_usage.sh &
  ./collect_network_activity.sh &
  sleep 60
done