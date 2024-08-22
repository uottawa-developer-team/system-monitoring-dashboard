#!/bin/bash

#get current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

primary_interface=$(route -n get default | grep interface | awk '{print $2}')

if [[ -n $primary_interface ]]; then #if not null

	#get network stats for primary interface (e.g. eth0)
	interface_stats=$(ifconfig "$primary_interface")

	#use awk to extract RX & TX bytes
	rx_bytes=$(echo "$interface_stats" | awk '/bytes/ {print $2}' | sed 's/bytes://')
	tx_bytes=$(echo "$interface_stats" | awk '/bytes/ {print $4}' | sed 's/bytes://')

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

if [[ $(wc -l < "$file" | awk '{print $1}') -gt 11520 ]]; then
	sed -i '2,9d' $file
fi