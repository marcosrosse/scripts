#!/bin/bash
set -e

## Create a POD to execute this script
## Create a payload.json with your unseal key and put it in a Kubernetes Secrets
## An alternative to Vault Enterprise

unseal (){

SEALED=$(curl -s $VAULT_ADDR/v1/sys/seal-status | jq '.sealed')

    if [ "$SEALED" = "true" ]
    then
      echo "Unsealing Vault..."
      curl -s -H "Content-Type: application/json" -XPUT $VAULT_ADDR/v1/sys/unseal --data '{"key": "'$(cat /tmp/payload.json)'"}'
      sleep 10
      echo "Vault is unsealed"
    else
      cat /dev/null
    fi

}
echo "Start"
while true; do
    unseal
    sleep 10
done;
