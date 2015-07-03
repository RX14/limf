#!/bin/env python
#Copyright 2015 lichinlich <lich@cock.li>
#Distributed under the terms of WTF Public License v2.
#See http://www.wtfpl.net/txt/copying for the full license text.
import sys
import re
import random
try:
    import requests
    import argparse
except ImportError:
    print("Install argparse and request libraries.")
    exit()

def UploadFiles(selected_file,selected_host):
    #uploads selected file to the host, thanks to the fact that
    #every pomf.se based site has pretty much the same architecture
    try:
        answer=requests.post(
            url=selected_host[0]+"upload.php",
            files={'files[]':open(selected_file,'rb')})
        return selected_file+" : "+selected_host[1]+(
        re.findall('"url":"(.+)",',answer.text)[0])
    except Exception as e:
        print(selected_file+" couldn't be uploaded to "+selected_host[0]+"\n")
              

def main():
    parser = argparse.ArgumentParser(
    description='Uploads selected file to working pomf.se clone')
    parser.add_argument('files',metavar='file',nargs='+',type=str,
    help = 'Files to upload')
    parser.add_argument('-c',metavar='host number',type=int,
    dest='host',default=random.randrange(0,4),
    help="Select hosting: 0 - 1339.cf,1 - bucket.pw,2 - xpo.pw,3 - pomf.cat.")
     
    args=parser.parse_args()
    #TODO check if clone is active or not.
    clone_list=[
    ["http://1339.cf/","http://a.1339.cf/"],
    ["https://bucket.pw/","https://dl.bucket.pw/"],
    ["http://xpo.pw/","http://u.xpo.pw/"],
    ["http://pomf.cat/","http://a.pomf.cat/"]
    ]
    #upload every file selected to random or chosen host
    for i in args.files:
        print(UploadFiles(i,clone_list[args.host]))

if __name__=='__main__':
    main()