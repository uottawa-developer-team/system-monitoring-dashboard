#!/bin/bash

# get current date & time
timestamp=$(date +"%Y-%m-%d %H:%M:%S") 

# get data
disk_data=$(df -h | awk '/^\/dev\// {print $1, $2, $3, $4, $5}')

# echo "$timestamp" >> "$(dirname "0")/../data/disk_data.log"
# echo "$disk_data" >> "$(dirname "0")/../data/disk_data.log"

#create a json representation of the data
create_json(){
    json=$(jq -n \
        --arg timestamp "$timestamp" \
        --argjson disk_data "$(echo "$disk_data" | jq -Rsn '
            [inputs | . / "\n" | map(
                split(" ") | {
                    device: .[0],
                    size: .[1],
                    used: .[2],
                    avail: .[3],
                    use_pcent: .[4]
                }
            )]
        ')" \
        '{
            timestamp: $timestamp,
            disk: $disk_data
        }')
    echo "$json"
}


# Path to file to save JSON data
file="$(dirname "$0")/../json_datalog/disk_data.json"

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