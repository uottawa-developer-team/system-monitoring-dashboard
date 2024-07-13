#!/bin/bash

#get current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

#get total & used memory
memoryOutput=$(free -m)
memoryLine=$(echo "$memoryOutput" | sed -n '2p') #get 2nd line of output

#parse data from line
totalMemory=$(echo "$memoryLine" | awk '{print $2}')
usedMemory=$(echo "$memoryLine" | awk '{print $3}')

cleanData=$(printf "Total: %sMB Used: %sMB" "$totalMemory" "$usedMemory")

#log the memory usage with the timestamp
echo "$timestamp" >> ../data/memory_usage.log
echo "$cleanData" >> ../data/memory_usage.log
