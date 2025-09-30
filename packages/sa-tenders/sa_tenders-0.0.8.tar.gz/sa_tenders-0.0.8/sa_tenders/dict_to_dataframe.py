'''
Programmer: Ntuthuko Hlela
Date created: 12.09.2025
Goal: Create a function that takes a dictionary and returns a pandas dataframe
'''

import pandas as pd
import numpy as np
import requests
import flatdict
import re
from pprint import pprint


def dict_to_dataframe(page_number: int=1, page_size:int=50, start_date:str="2020-01-01", end_date:str="2024-12-31", currently_advertised=True, awarded=True, *args, **kwargs):
    '''
    Pulling the data from sa_tenders, flattening the dictionary and then converting it into a pandas dataframe.
    '''
    try:

        #Pulling the data from sa_tenders
        url = f"https://ocds-api.etenders.gov.za/api/OCDSReleases?PageNumber={page_number}&PageSize={page_size}&dateFrom={start_date}&dateTo={end_date}"
        get = requests.get(url)
        raw_data = get.json()
        tenders = (raw_data["releases"])
        if len(tenders) == 0:
            exit()
    except:
        print("I could not find the tenders. Try changing the date range and/or page size.")
        exit()


    #creating the meta data
    meta_data = []
    for i in ["uri", "version", "publishedDate", "license", "publicationPolicy"]:
        meta_data.append({i: raw_data[i]})


    #flattening the data
    list_flattened_tenders = []
    for i in tenders:
        flattened_tender = flatdict.FlatterDict(i, delimiter="_")
        list_flattened_tenders.append(dict(flattened_tender))
    full_data_dataframe = pd.DataFrame(list_flattened_tenders)

    #removing columns that are derived from orig keys. I.e., {x: [{n1:1, n2:2}]}, I will remove x since I now have x_n1 and x_n2.
    for i in full_data_dataframe.columns:
        c = re.findall(r"_", i)
        if len(c) > 0:
            original_key = re.match(r"[a-z]*", i).group()
            if original_key in full_data_dataframe.columns:
                full_data_dataframe.drop(original_key, inplace=True, axis=1)

    #adding the meta data to the dict
    meta_vars = ["uri", "version", "publishedDate", "license", "publicationPolicy"]
    for i in meta_vars:
        full_data_dataframe.insert(meta_vars.index(i), column=str(i), value=raw_data[i])
        #meta_data.append({i: [raw_data[i]]*len(full_data_dataframe)})


    #more meta data
    full_data_dataframe.insert(0, column="publisher_name", value=(str(raw_data["publisher"]["name"])))
    full_data_dataframe.insert(1, column="publisher_uri", value=(raw_data["publisher"]["uri"]))
    full_data_dataframe.insert(len(meta_vars)+1, column="links_next", value=(raw_data["links"]["next"]))


    return {"meta_data": meta_data, "raw_data": raw_data, "full_data_dataframe": full_data_dataframe}


