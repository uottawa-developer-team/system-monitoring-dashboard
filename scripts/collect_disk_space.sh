#!/bin/bash

# get current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S") 

# get data
disk_data=$(df -h --output=source,size,used,avail,pcent | grep "^/dev/") 

echo "$timestamp" >> ../data/disk_data.log
echo "$disk_data" >> ../data/disk_data.log

#create a json representation of the data
create_json(){
	
	json=$(jq -n \
		--arg timestamp "$timestamp" \
        --arg disk_data "$disk_data" \
        '{
            timestamp: $timestamp,
            disk: ($disk_data | split("\n") | map(
                capture("^(?<device>/dev/[^ ]+) +(?<size>[^ ]+) +(?<used>[^ ]+) +(?<avail>[^ ]+) +(?<use_pcent>[^ ]+)$") | 
                {
                    device: .device,
                    size: .size,
                    used: .used,
                    avail: .avail,
                    use_pcent: .use_pcent
                }
            )),
	
		}')
	echo "$json"	
}


# Save data to files
create_json >> "../json_datalog/disk_data.json"


