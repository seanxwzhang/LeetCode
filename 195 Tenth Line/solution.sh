#!/usr/bin/env bash
# set -x
input="./file.txt"
counter=1
while IFS= read -r line
do
    if [ $counter -eq 10 ]
    then
        echo "$line"
        exit 0
    fi
((counter++))
done < "$input"