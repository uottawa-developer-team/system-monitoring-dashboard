#!/bin/bash

# get current date & time
echo $(date +"%Y-%m-%d %H:%M:%S") >> ../data/cpu_usage.log

# get cpu data
top -b -n 1 | head -n 5 | grep "Cpu" >> ../data/cpu_usage.log
