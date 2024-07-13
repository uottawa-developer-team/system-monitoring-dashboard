#!/bin/bash

# get current date & time
echo $(date +"%Y-%m-%d %H:%M:%S") >> ../data/disk_space.log

# get data
df -h | grep "/dev/sd" >> ../data/disk_space.log

