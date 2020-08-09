#!/usr/bin/python 
#-*-coding：utf-8 -*- 

'''
# -------------------------------------------------------------------------------
# Purpose:     
#
# Author:      青衫少年春归也
#
# Created:     
#
# Copyright:   
# -------------------------------------------------------------------------------
'''


import requests

info = []
while 10:
    res = requests.get(f'https://api.lovelive.tools/api/SweetNothings/{100000000}/Serialization/Json')
    content = res.json()
    data = content.get("returnObj", [])
    with open("story2.txt", "a", encoding='utf-8') as f:
        for one in data:
            if one not in info:
                info.append(one)
                f.write(one)
                f.write("\n\n")