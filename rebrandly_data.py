#!/usr/bin/env python
# coding: utf-8
# first install all required libraries
# import all required libraries
#######################################################

import requests
import csv
import pandas as pd
import json
import os
import isodate

from datetime import datetime



# link count by api

url = "https://api.rebrandly.com/v1/links/count"

headers = {
    "Accept": "application/json",
    "workspace": "your workapace",
    "apikey": "your apikey"
}
# count numbers link from rebrandely api
def link_counts():
    url = "https://api.rebrandly.com/v1/links/count"

    headers = {
        "Accept": "application/json",
        "workspace": "your workspac",
        "apikey": "your apikey"
    }

    response = requests.get(url, headers=headers)
    
    return response.json()
    


link_count=link_counts()['count']

link_count




# calculate how many time to iterat ,25 is thme maximun number of links you can get from rebrandly api 
if link_count %  25 != 0:
    iterat=int(link_count/25)+1
else:
    iterat=int(link_count/25)
iterat




# return last id 

def last_id(x):
    scraped_item=len(x)
    last=x[scraped_item-1]["id"]
    return last

lastid=""
a=[]
# return data from rebrandly api
for i in range(iterat) :
    

    url_first = "https://api.rebrandly.com/v1/links?orderBy=createdAt&orderDir=desc&limit=none&last="+lastid


    headers = {
        "Accept": "application/json",
        "workspace": "********",
        "apikey": "************"
    }
    links_response = requests.get(url_first, headers=headers,data={})
    links_json= links_response.json()
    lastid=last_id(links_json)
    #add all date to list
    a+=links_json
# save a list in json file    
with open('rebrandly_links.json', 'w') as outfile:
    json.dump(a, outfile)

  
   

# convert to dataframe

df_rep = pd.json_normalize(
    a,'tags',['id','title','clicks','slashtag','destination','createdAt','updatedAt','shortUrl','domainName','status',['domain','fullName'],['creator','fullName']],errors='ignore', record_prefix='_')



# rename columns to avoid conflict

df_rep.rename(columns={'domain.fullName':'domain_fullName','creator.fullName':'creator_fullName'},inplace=True)
df_rep['clicks'] = df_rep['clicks'].astype(str)

# add scraped time as a column

df_rep['scraped_time']= datetime.today().strftime('%Y-%m-%d %H:%M:%S')


# save in gbq

df_rep.to_gbq(destination_table="Rebrandly.Rebrandly_Data",project_id="********", if_exists="replace")







