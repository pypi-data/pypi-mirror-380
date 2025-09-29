'''
Programmer: ntuthuko hlela
Goal: storing old code that I deleted from the main pys. It helps me avoid going to version history.
'''

'''
from bs4 import BeautifulSoup as bs
import requests
import json
import pandas as pd

#import functions
import functions


class sa_tenders():

   
    #This is the main sa tenders class. It contains all the library methods and attributes.
    


    def __init__(self, page_number: int=1, page_size:int=500, start_date:str="2024-01-01", end_date:str="2024-12-31", currently_advertised=True, awarded=True, *args, **kwargs):

        
        #The init pulls the data from the etenders api and stores it in a global environment so that all the
        #library functions can access it easily.
        

        self.raw_data = functions.pull_data(page_number, page_size, start_date, end_date, currently_advertised, awarded, *args, **kwargs)
        if self.raw_data[0] == "failed":
            exit()
        self.pulled_data = self.raw_data[1]["releases"]




    def Search (self, ocid=None, id=None, tender_number = None):

        
        #Searching for a specific tender by ocid, id or tender number. Returns the list of all the
        #matching tenders. You can use the dot notation to get the specif detail of a tender/s
        

        tenders = functions.vertical_pov(raw_data=self.pulled_data, ocid=ocid, id=id, tender_number = tender_number)
        print(tenders)
        if tenders != "No tender was found.":
            class vertical_search():
                all_matches = tenders
                number_of_matches = len(tenders)
                ocid = []
                id = []
                date = []
                tag = []
                initiationType = []
                tender = []
                planning = []
                parties = []
                buyer = []
                language = []
                awards = []
                contracts = []
                print(all_matches)

                for i in all_matches:
                    ocid.append(i["ocid"])
                    id.append(i["id"])
                    date.append(i["date"])
                    tag.append(i["tag"])
                    initiationType.append(i["initiationType"])
                    tender.append(i["tender"])
                    planning.append(i["planning"])
                    parties.append(i["parties"])
                    buyer.append(i["buyer"])
                    language.append(i["language"])
                    awards.append(i["awards"])
                    contracts.append(i["awards"])

            return vertical_search()
        else:
            return "No matches found"


    def Awarded(self):
        
        #Only awarded tenders.
        
        class awarded_tenders():
            all_matches = []
            suppliers = []
            for i in self.pulled_data:
                if len(i["awards"]) > 0:
                    all_matches.append(i)

                    for j in i["awards"]:
                        suppliers.append(j["suppliers"])

        return awarded_tenders()





h = sa_tenders()
print(h.Search(tender_number="DSM 3/26").parties)
#print(h.Search(tender_number= "DSM 3/26"))
'''





'''

import pandas as pd
import numpy as np
import requests
import json
from operator import itemgetter

url = f"https://ocds-api.etenders.gov.za/api/OCDSReleases?PageNumber={1}&PageSize={100}&dateFrom={"2024-01-01"}&dateTo={"2024-01-12"}"


#filtering the data
def pull_data(page_number: int=1, page_size:int=500, start_date:str="2024-01-01", end_date:str="2024-12-31", currently_advertised=True, awarded=True, *args, **kwargs):
    #pulling the raw data
    try:
        url = f"https://ocds-api.etenders.gov.za/api/OCDSReleases?PageNumber={page_number}&PageSize={page_size}&dateFrom={start_date}&dateTo={end_date}"
        get = requests.get(url)

        if get.status_code == 200:
            # clean the data
            data = get.json()
            return ["passed", data]

        elif get.status_code != 200:
            print(f"There was an error calling the API. The status code is {get.status_code}")
            return ["failed", 0]


    except Exception as e:
        error_message = e
        print(f"There was an error, here is the error message: \n {error_message}")
        return ["failed", 0]



data = pull_data()[1]

with open ("output_file.json", "w") as file:
    json.dump(data, file, indent=4)


def vertical_pov(raw_data, ocid=None, id=None, tender_number = None):
    # looking at all the tender data (one tender at the time) 
    tenders = []
    for i in raw_data:
        ocid_x = i["ocid"]
        id_x = i["id"]
        tender_number_x = i["tender"]["title"]

        if ocid_x == str(ocid) or id_x == str(id) or tender_number_x == str(tender_number):
            tenders.append(i)
            return tenders

    return "No tender was found."

tenders = []
all_matches = []



def final_data(dicts):

    dict_holder = list(dicts.items())
    final = []

    while len(dict_holder) > 0:

        # 1) pop the last item on the list and check if its value is a dict or not
        popped = dict_holder.pop()
        if isinstance(popped[1], (dict, list)):

            if isinstance(popped[1], dict):
                # 2) if a dict, take the items
                items = list(popped[1].items())
                main_key = popped[0]


            elif isinstance(popped[1], list):
                main_key = popped[0]
                for i in popped[1]:
                    if isinstance(i, dict):
                        items = list(i.items())
                    elif isinstance(i, (str, int, float)):
                        constructed_tuple = (main_key, i)
                        final.append(constructed_tuple)
                        continue

                    else:
                        #this happens when the list is empty
                        continue


            # 3) iterate through the items just to change the key names to reflect parent keys
            new = []
            for i in items:
                tuple_to_list = list(i)
                tuple_to_list[0] = str(main_key) + "_" + str(tuple_to_list[0])
                list_to_tuple = tuple(tuple_to_list)
                # print(list_to_tuple)
                new.append(list_to_tuple)

            # 4) add the  items with dict values to the dict_holder to test they themselves have a dict value
            dict_holder.extend(new)


        else:
            # if not a dict, append the item popped item
            final.append(popped)



    #dealing with duplicated names
    keys_original = [i[0] for i in final]
    final_items = []
    keys = []

    for i in final:
        count_occurences = keys_original.count(i[0])

        if count_occurences > 1:
            in_keys = keys.count(i[0])
            keys.append(i[0])
            suffix = (count_occurences + 1) - (count_occurences - in_keys)  #just to keep the sequence!

            temp_item = list(i)
            temp_item[0] = f'{i[0]}_{suffix}'
            final_item = tuple(temp_item)
            final_items.append(final_item)

        elif count_occurences == 1:
            final_items.append(i)

        else:
            print("I can not find the key. Fatal. I am exiting the code.")
            exit()

    return final


print(final_data(tenders))


dict1 = {"name": "John", "age": 30,
         "test_list": [1, 2, {"datahub": "datafirst", "location":"uct", "uni": {"kzn": "ukzn", "campuses": ["Howard", "Westville", "pmb"], "gauteng": "uj",
                            "kk": {"p":1}}}], "test_dict": {"title": "developer", "company": "google",
                            "language": {"ds": "python", "l": ["lll"], "en": "english", "africa": {"sa": "en", "egypt": "arabic"}}}}



Programmer: Ntuthuko Hlela
Goal: Cleaning the raw data from the SA tenders API. Make this a table


import pandas as pd
import numpy as np
import requests
import json
import math


def data_pull(page_number: int=1, page_size:int=500, start_date:str="2024-01-01", end_date:str="2024-12-31", currently_advertised=True, awarded=True, *args, **kwargs):
    url = f"https://ocds-api.etenders.gov.za/api/OCDSReleases?PageNumber={page_number}&PageSize={page_size}&dateFrom={start_date}&dateTo={end_date}"
    get = requests.get(url)
    return get.json()

tenders = (data_pull()["releases"])
x = []
for i in tenders:
    x.append(len(i["awards"]))
print(np.array(x).max())



data = data_pull()
with open ("output_file.json", "w") as file:
    json.dump(data, file, indent=4)


def json_to_dataframe():
    json_data = data_pull()
    tenders = json_data["releases"]

    #initializing and setting up the dataframe
    str_global_vars = ["ocid", "id", "date", "initiationType", "language"]
    df = pd.DataFrame(tenders)[str_global_vars] #only keeping the str vars for now

    #tag
    df["tag"] = [i["tag"][0] or None for i in tenders]

    #tender
    for sub_var in ["id", "title", "status", "mainProcurementCategory","description"]:
        col_name = "tender_" +  str(sub_var)
        df[col_name] = [i["tender"][str(sub_var)] or None for i in tenders]

    df["tender_additionalProcurementCategories"] = [i["tender"]["additionalProcurementCategories"][0] or None for i in tenders]
    df["tender_value_amount"] = [i["tender"]["value"]["amount"] or None for i in tenders]
    df["tender_value_currency"] = [i["tender"]["value"]["currency"] or None for i in tenders]

    #documents
    for sub_var in ["id","documentType", "title", "description", "url", "datePublished", "dateModified", "format", "language"]:
        col_name = "tender_documents" + str(sub_var)
        df[col_name] = [i["tender"]["documents"][0][str(sub_var)] or None for i in tenders]



    #buyer
    df["buyer_id"] = [i["buyer"]["id"] or None for i in tenders]
    df["buyer_name"] = [i["buyer"]["name"] or None for i in tenders]


    df.to_excel("dataframe_test.xlsx")


#json_to_dataframe()


    # strings to floats
    floats_columns = ["tender_value_amount", "awards_0_value_amount"]  #input the str_to_float variables here
    for i in floats_columns:
        try:
            dataframe[i] = dataframe[floats_columns].map(lambda x:float(x), na_action="ignore")
            print(True)
        except:
            comment = f'{i} is missing, so, skip.'
            print(comment)
    #dataframe[floats_columns] = dataframe[floats_columns].map(lambda x:float(x), na_action="ignore")

'''

