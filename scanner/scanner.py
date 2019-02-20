import re
import subprocess
import json
import os
import requests

arp_out =subprocess.check_output(['arp'])

while True:
    macs_list = re.findall(r"((\w{2,2}\:{0,1}){6})", arp_out)

    macs_dict = {
        "macs" : []
        }

    for tup in macs_list:
    mac = tup[0] 
    macs_dict["macs"].append(mac.upper())

    endpoint = os.environ['WH_UPDATE_ENDPOINT']
    print(endpoint)

    response = requests.post(endpoint, json = macs_dict)
    print(response.text)
