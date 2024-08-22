#!/bin/bash

# Get the current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

# Get the CPU data
cpu_data=$(top -l 1 | grep "CPU usage")

# # Write into the log file
# echo $timestamp >> "$(dirname "$0")/../data/cpu_usage.log"
# echo $cpu_data >> "$(dirname "$0")/../data/cpu_usage.log"

if [[ ! -n $cpu_data ]]; then #if null
	cpu_data="0.0 0.0 0.0"
else #if not null
	# parse data for easier readability by create_json function
	cpu_data=$(echo "$cpu_data" | sed 's/,/ /g' | awk '{print $3,$5,$7}')
	cpu_data=$(echo "$cpu_data" | sed 's/%//g')
fi

# Function to create JSON data
create_json(){
	
	json=$(jq -n \
		--arg timestamp "$timestamp"\
		--arg cpu_data "$cpu_data"\
		'{
			timestamp: $timestamp,
			cpu: {
				user: ($cpu_data | split(" ")[0]),
				system: ($cpu_data | split(" ")[1]),
				idle: ($cpu_data | split(" ")[2]),
			}
		}')
	echo "$json"	
}



# Path to file to save JSON data

file="$(dirname "$0")/../json_datalog/cpu_usage.json"

# Hard-coding Edge cases for the JSON format file

# Create the file if it doesn't exist
if [ -f "$file" ]; then
    if [[ $(head -n 1 "$file") != "[" ]]; then
        echo "[" > $file
        create_json >> $file
    else
        if [[ $(tail -n 1 $file)  == "]" ]]; then
            sed -i '$d' $file
        fi
        last_line=$(tail -n 1 "$file")
        last_line+=","
        sed -i "$ s/.*/$last_line/" "$file"
        create_json >> $file
    fi
else
    # file does not exist, create it
    echo "[" > $file
    create_json >> $file
fi

echo "]" >> $file

# CP
if [[ $(wc -l < "$file" | awk '{print $1}') -gt 11520 ]]; then
	sed -i '2,9d' $file
fi

find "$(dirname "$0")/../json_datalog/" -type f -name 'sed*' -delete