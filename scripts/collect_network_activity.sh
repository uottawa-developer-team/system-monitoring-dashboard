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

# Save data to files
create_json >> "../json_datalog/network_data.json"
