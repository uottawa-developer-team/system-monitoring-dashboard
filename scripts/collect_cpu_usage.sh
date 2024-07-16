#!/bin/bash

# Get the current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

# Get the CPU data
cpu_data=$(top -b -n 1 | head -n -5 | grep "Cpu")

# Write into the log file
echo $timestamp >> "../data/cpu_usage.log"
echo $cpu_data >> "../data/cpu_usage.log"

cpu_data=$(echo "$cpu_data" | awk '{print $2,$4,$6,$8,$10,$12,$14,$16}')

create_json(){
	
	json=$(jq -n \
		--arg timestamp "$timestamp"\
		--arg cpu_data "$cpu_data"\
		'{
			timestamp: $timestamp,
			cpu: {
				user: ($cpu_data | split(" ")[0]),
				system: ($cpu_data | split(" ")[1]),
                		nice: ($cpu_data | split(" ")[2]),
                		idle: ($cpu_data | split(" ")[3]),
                		wait: ($cpu_data | split(" ")[4]),
                		hi: ($cpu_data | split(" ")[5]),
                		si: ($cpu_data | split(" ")[6]),
                		st: ($cpu_data | split(" ")[7])			
			}	
	
		}')
	echo "$json"	
}

# Save data to files

create_json >> "../json_datalog/cpu_usage.json"
