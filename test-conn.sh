#!/bin/bash

#How to use:
## Create a file with IP:PORT or DNS:PORT, exemple:
## 127.0.0.1:1521
## 127.0.0.1:443
## 127.0.0.1:9200

#How to execute: 
## ./test-conn.sh -l list.txt -t 2 -o output.csv

while getopts l:o:t: flag
do
  case "${flag}" in
    l) list=${OPTARG};;
    o) output=${OPTARG};;
    t) timeout=${OPTARG};;
  esac
done

file=$list

echo "host_and_port,status" > output.txt

while IFS= read -r line
do
   echo -e '\x1dclose\x0d'|curl --connect-timeout $timeout telnet://$line -vv
   if [ $? -eq 0 ]; then
    echo -e "$line,success" >> $output
   else
    echo -e "$line,failed" >> $output
   fi
done <"$file"
