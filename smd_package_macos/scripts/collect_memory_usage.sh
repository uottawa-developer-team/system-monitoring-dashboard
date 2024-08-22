#!/bin/bash

#get current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

#get total & used memory
memory_data=$(top -l 1 | grep "PhysMem:") #get line of memory

# Parse data from top output
used_memory=$(echo "$memory_data" | awk '{print $2}' | sed 's/M//')
free_memory=$(echo "$memory_data" | awk '{print $6}' | sed 's/M//')

# If the memory data is null, set default values
if [[ -z "$memory_data" ]]; then
    memory_data="0 0"
else
    # Prepare memory data for JSON
    memory_data="$used_memory $free_memory"
fi

#create a json representation of the data
create_json(){
	
	json=$(jq -n \
		--arg timestamp "$timestamp"\
		--arg memory_data "$memory_data"\
		'{
			timestamp: $timestamp,
			memory: {
                used: ($memory_data | split(" ")[0]),
                free: ($memory_data | split(" ")[1]),
			}	
	
		}')
	echo "$json"	
}

# Path to file to save JSON data
file="$(dirname "$0")/../json_datalog/memory_usage.json"

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

if [[ $(wc -l < "$file"| awk '{print $1}') -gt 10100 ]]; then
	sed -i '2,8d' $file
fi