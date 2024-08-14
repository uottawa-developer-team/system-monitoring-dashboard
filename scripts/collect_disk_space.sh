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


# Path to file to save JSON data
file="../json_datalog/disk_data.json"

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

num=$(echo "$disk_data" | grep "^/dev/" | wc -l)
endnum=$((6 + 7 * num))

if [[ $(wc -l <"$file") -gt $(($((endnum - 1)) * 240)) ]]; then
   sed -i "2,${endnum}d" $file
fi