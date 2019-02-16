#!/bin/bash
while :
do

sudo nmap -sP -n 192.168.0.0/24 | grep MAC | cut -c 14-30 >> macs.txt
sed -i ':a;N;$!ba;s/\n/\,/g' macs.txt
sed -i '1s/^/[/' macs.txt
echo "]" >>  macs.txt
curl -X POST --data "@macs.txt" $WHOSHOME_API
rm macs.txt
done

