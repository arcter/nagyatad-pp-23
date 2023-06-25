#!/bin/env python

import requests
import ipaddress
import os
import re

def is_up(host):
    response = os.system("ping -c 1 " + host)
    #and then check the response...
    if response == 0:
        return True
    else:
        return False

def positive_score(ip):
    url="http://["+str(ip)+"]:8080/describe"
    r=requests.get(url)
    mj=messages.json()
    if mj["score"]>0:
        return True
    return False

def str_array_equal(array1, array2):
    array1=sorted(set(array1))
    array2=sorted(set(array2))
    if len(array1)!=len(array2):
        return False
    for i in range(0,len(array1)):
        if array1[i]!=array2[i]:
            return False
    return True

if __name__=="__main__":
    ind=5830860
    while True:
        messages=requests.get("https://tutter.pproj.dev/api/post?after_id="+str(ind))
        mj=messages.json()
        ip_list=[]
        file1 = open('ip/ip_list.txt', 'r')
        Lines = file1.readlines()
        for line in Lines:
            ip_list.append(line.strip())
        file1.close()
        for message in mj:
            if message["tags"]== ['important', 'target', 'addr']:
                text=message["text"].split()
                for word in text:
                    try:
                        a=ipaddress.ip_address(word)
                        ip_list.append(str(a))
                    except:
                        pass
            if message["author"]["name"] == "ignorme":
                pass
            if message["author"]["name"] == "arcter":
                pass
            if message["author"]["name"] == "ollescram":
                text=message["text"].split()
                for word in text:
                    try:
                        a=ipaddress.ip_address(word)
                        ip_list.append(str(a))
                    except:
                        pass
            else:
                text=message["text"].split('\'')
                for word in text:
                    try:
                        a=ipaddress.ip_address(word)
                        ip_list.append(str(a))
                    except:
                        pass
        ip_list=sorted(set(ip_list))
        print(ip_list)
        bad_list=[]
        for ip in ip_list:
            if not is_up(ip):
                bad_list.append(ip)
            else:
                if not positive_score(ip):
                    bad_list.append(ip)
        for ip in bad_list:
            ip_list.remove(ip)
        print(ip_list)
        f=open("ip/ip_list.txt","w")
        for ip in ip_list:
            f.write(ip+"\n")
        f.close()
        # print(mj[-1])
        # print(mj[-1]["id"])
        id=mj[-1]["id"]
        print(id)