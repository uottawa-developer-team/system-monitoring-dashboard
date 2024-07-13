#!/bin/bash

#get current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S")

#run ifconfig to get network info
network_info=$(ifconfig)

#use grep to filter lines starting with non-space or newline chars (aka the interface names)
interface_lines=$(echo "$network_info" | grep -E '^[a-zA-Z0-9]')

#use awk to extract interface names
interfaces=$(echo "$interface_lines" | awk '{print $1}')

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
clean_data="Interfaces:\n$interfaces\nPrimary Interface: $primary_interface\nStats: $network_stats"

#log network activity with timestamp
echo "$timestamp" >> ../data/network_activity.log
echo -e "$clean_data" >> ../data/network_activity.log
