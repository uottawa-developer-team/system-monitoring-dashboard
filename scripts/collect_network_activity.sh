#!/bin/bash

#get current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

primary_interface=$(ip route | grep default | awk '{print $5}') #use ip command to get primary network interface

if [[ -n $primary_interface ]]; then #if not null

	#get network stats for primary interface (e.g. eth0)
	interface_stats=$(ifconfig "$primary_interface")

	#use awk to extract RX & TX bytes
	rx_bytes=$(echo "$interface_stats" | awk '/RX packets/ {print $5}') #received bytes
	tx_bytes=$(echo "$interface_stats" | awk '/TX packets/ {print $5}') #transmitted bytes

	#combine RX & TX bytes into stats string
	network_stats="$interface_name RX bytes: $rx_bytes TX bytes: $tx_bytes"

else #if null
	network_stats="ERROR: No primary interface detected"
fi

#combine interfaces & stats into clean data string
clean_data="Primary Interface: $primary_interface\nStats: $network_stats"

#log network activity with timestamp
echo "$timestamp" >> ../data/network_activity.log
echo -e "$clean_data" >> ../data/network_activity.log


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
file="../json_datalog/network_data.json"

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