#!/bin/bash

#get current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

#get total & used memory
memory_data=$(free -m | grep "Mem") #get line of memory

#parse data from line
total_memory=$(echo "$memory_data" | awk '{print $2}')
used_memory=$(echo "$memory_data" | awk '{print $3}')

clean_data=$(printf "Total: %sMB Used: %sMB" "$total_memory" "$used_memory")

#log the memory usage with the timestamp
echo "$timestamp" >> ../data/memory_usage.log
echo "$clean_data" >> ../data/memory_usage.log

memory_data=$(echo "$memory_data" | awk '{print $2,$3,$4,$5,$6,$7}')

#create a json representation of the data
create_json(){
	
	json=$(jq -n \
		--arg timestamp "$timestamp"\
		--arg memory_data "$memory_data"\
		'{
			timestamp: $timestamp,
			memory: {
				total: ($memory_data | split(" ")[0]),
                used: ($memory_data | split(" ")[1]),
                free: ($memory_data | split(" ")[2]),
                shared: ($memory_data | split(" ")[3]),
                buff_cache: ($memory_data | split(" ")[4]),
                available: ($memory_data | split(" ")[5])		
			}	
	
		}')
	echo "$json"	
}

# Save data to files
create_json >> "../json_datalog/memory_usage.json"
