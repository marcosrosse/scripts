#!/bin/bash

#How to use:
## Create a csv file with IP, PORT or DNS, PORT. Exemple:
## host,port
## 127.0.0.1,1521
## 127.0.0.1,443
## 127.0.0.1,9200

#How to execute:
## ./test-conn.sh -l list.csv -t 2

while getopts l:t: flag
do
  case "${flag}" in
    l) list=${OPTARG};;
    t) timeout=${OPTARG};;
  esac
done

file=$list

echo "host,port,status" > output.csv

while IFS="," read -r col1 col2
do
   echo -e "Requesting host $col1 on port $col2\n"
   echo -e '\x1dclose\x0d'|curl --connect-timeout $timeout telnet://$col1:$col2 --silent > /dev/null
   if [ $? -eq 0 ]; then
    echo -e "$col1,$col2,success" >> output.csv
   else
    echo -e "$col1,$col2,failed" >> output.csv
   fi
done <"$file"

# To remove the second line of the file
sed -i '2d' output.csv
