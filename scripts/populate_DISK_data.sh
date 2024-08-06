#!/bin/bash

while true; do
  ./collect_disk_space.sh &
  sleep 3600
done