#!/bin/bash

while true;
do
sudo nmap -sP -n 192.168.0.0/24 | grep MAC | cut -c 14-30 > macs.json
sed -i ':a;N;$!ba;s/\n/\",\"/g' macs.json
sed -i '1s/^/{"macs":["/' macs.json
echo "\"]}" >>  macs.json
sed -i ':a;N;$!ba;s/\n//g' macs.json
curl --header "Content-type: application/json"\
       --request POST \
       --data "@macs.json" \
       --url $WH_UPDATE_ENDPOINT
sleep 10s
done
