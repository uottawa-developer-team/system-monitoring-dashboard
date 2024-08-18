#!/bin/bash

# Get the current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

# Get the CPU data
cpu_data=$(top -b -n 1 | head -n -5 | grep "Cpu")

# Write into the log file
echo $timestamp >> "$(dirname "$0")/../data/cpu_usage.log"
echo $cpu_data >> "$(dirname "$0")/../data/cpu_usage.log"

if [[ ! -n $cpu_data ]]; then #if null
	cpu_data="%Cpu(s): 0.0 us, 0.0 sy, 0.0 ni, 0.0 id, 0.0 wa, 0.0 hi, 0.0 si, 0.0 st"
else #if not null
	# parse data for easier readability by create_json function
	cpu_data=$(echo "$cpu_data" | sed 's/,/ /g' | awk '{print $2,$4,$6,$8,$10,$12,$14,$16}')
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
if [[ $(wc -l < "$file" | awk '{print $1}') -gt 18740 ]]; then
	sed -i '2,14d' $file
fi

find "$(dirname "$0")/../json_datalog/" -type f -name 'sed*' -delete