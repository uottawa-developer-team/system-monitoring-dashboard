#!/bin/bash

for i in {1..30}; do
 ./collect_cpu_usage.sh
 ./collect_memory_usage.sh
  sleep 60
done