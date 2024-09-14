#!/bin/bash

#get current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

# primary_interface=$(ip route | grep default | awk '{print $5}') #use ip command to get primary network interface

primary_interface=$(ip route | grep default | sort -k5 -n | head -n 1 | awk '{print $5}')

if [[ -n $primary_interface ]]; then #if not null

	rx_bytes=$(cat /sys/class/net/"primary_interface"/statistics/rx_bytes)
	rx_bytes=$(cat /sys/class/net/"primary_interface"/statistics/tx_bytes)

else #if null
	primary_interface="No Primary interface detected"
	rx_bytes=0
	tx_bytes=0
fi

#create a json representation of the data
create_json(){
	
	json=$(jq -n \
		--arg timestamp "$timestamp"\
		--arg primary_interface "$primary_interface"\
		--arg rx_bytes "$rx_bytes"\
		--arg tx_bytes "$tx_bytes"\
		'{
			timestamp: $timestamp,
			network: {
				primary_interface: ($primary_interface),
                rx_bytes: $rx_bytes,
                tx_bytes: $tx_bytes,	
			}
		}')
	echo "$json"	
}

# Path to file to save JSON data
file="$(dirname "$0")/../json_datalog/network_data.json"

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

if [[ $(wc -l < "$file" | awk '{print $1}') -gt 10100 ]]; then
	sed -i '2,9d' $file
fi
