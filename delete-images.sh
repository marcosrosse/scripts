#!/bin/bash

#How to use:
## ./delete-images.sh OR ./delete-images.sh <A NAME OR PATTERN TO GREP>
## flag is to search for all images with the name you want to search.

docker images | grep "$1" | tr -s ' ' > images.txt

sed -i "/\b\(maven\|alpine\|jenkins\|nexus\|azurecr\|gitlab\|nginx\)\b/d" images.txt # remove everything with these names

cat images.txt|cut -d ' ' -f 3 > imagestodelete.txt
rm images.txt

file=imagestodelete.txt

while IFS= read -r line
do
  echo -e "Deleting image $line\n"
  docker rmi -f $line

  if [ $? -eq 0 ]; then
      echo -e "Image $line deleted with success" >> output.txt
  else
      echo -e "Failed while deleting image $line" >> output.txt
  fi

done <"$file"
