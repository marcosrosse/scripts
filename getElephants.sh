#!/usr/bin/env bash

## A simple script to copy files from an OpenShift POD.
## It's recommended to split the file in the POD with the command: split -b 1m <FILE TO BE SPLITED>

FILENAME="files.txt"
FILESPATH="COPY"
POD_NAME="jmeter-master-0"

function createAndGetFilename {
  oc exec $POD_NAME  -- find $FILESPATH -type f -name 'x*' -printf '%f\n' > $FILENAME
}

function getElephantsFile {
  CONTENT=$(cat $FILENAME)
  for line in $CONTENT
    do
      echo "-=-=- COPYING $line -=-=-"
      oc cp $POD_NAME:/$FILESPATH/$line $line
      echo ""
      if $? == 0; then
        echo "$line FILE COPIED SUCCESSFULY"
        echo ""
      else
        echo "ERROR WHILE COPYING THE FILE $line, PLEASE TRY AGAIN LATTER"
        echo "$line" >> error.txt
        echo ""
      fi
    done
}
createAndGetFilename
getElephantsFile
