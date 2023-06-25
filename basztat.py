#!/bin/env python

import requests
import json
import ipaddress
import random
import time
import _thread
import base64


def basztat0():
    while True:
        message="Ahoy amigo we have we have IP address: "
        network=ipaddress.ip_network('fd23::/64')
        upper_limit=network.num_addresses
        r=random.randint(0,upper_limit)
        ip_address=network[r]
        print(ip_address)
        print(message+str(ip_address))
        text=message+str(ip_address)
        payload={"author": "arcter","text":text }
        r=requests.post("https://tutter.pproj.dev/api/post", data=json.dumps(payload))
        time.sleep(random.randint(3,15))

def basztat1():
        while True:
            users=["rootka_admian",'marcsello','robotka']
            for user in users:
                text="Brrrrrrr..........."
                if user=="marcsello":
                    text="covfefe\nI'm very verified dear sire!"
                payload={"author": user,"text":text }
                r=requests.post("https://tutter.pproj.dev/api/post", data=json.dumps(payload))
                time.sleep(random.randint(1,3))

def basztat2():
        while True:
            text="You killed me "
            j=requests.get("https://gameinfo.albiononline.com/api/gameinfo/events?limit=1&offset=0")
            rj=j.json()
            killer=rj[0]["Killer"]["Name"]
            dead=rj[0]["Victim"]["Name"]
            text=text+killer+"--"+dead
            payload={"author": "arcter","text":text }
            r=requests.post("https://tutter.pproj.dev/api/post", data=json.dumps(payload))
            time.sleep(1)

if __name__=="__main__":
    try:
        _thread.start_new_thread( basztat0, () )
        _thread.start_new_thread( basztat1, ()  )
        _thread.start_new_thread( basztat2, ()  )
    except:
        print("Error: unable to start thread")

    while 1:
        pass