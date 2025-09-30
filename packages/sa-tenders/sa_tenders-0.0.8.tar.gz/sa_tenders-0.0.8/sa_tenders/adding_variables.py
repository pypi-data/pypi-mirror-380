'''
Programmer: Ntuthuko Hlela
Goal: Creating / adding variables (making the data more useful)
'''

import pandas as pd
import numpy as np
import requests
import json
import math
import math


import dict_to_dataframe
import data_cleaning

#data = (dict_to_dataframe.dict_to_dataframe(page_size=10))
#data_cleaned = data_cleaning.data_cleaning(data["full_data_dataframe"])


def meta_variables(data):

    # Metadata
    var_exists = {}
    for i in ["awards_0_suppliers_0_name", "buyer_name", "awards_0_value_amount"]:
        try:

            exists = len(data[str(i)])
            var_exists[i] = True
        except:
            var_exists[i] = False

    unique_buyers = list(set(data["buyer_name"])) if var_exists["buyer_name"] == True else None
    number_of_unique_buyers = len(unique_buyers) if var_exists["buyer_name"] == True else None


    unique_sellers = list(set(data["awards_0_suppliers_0_name"])) if var_exists["awards_0_suppliers_0_name"] == True else None
    number_of_unique_sellers = len(unique_sellers) if var_exists["awards_0_suppliers_0_name"] else None
    total_money_spent = sum([float(i) for i in data["awards_0_value_amount"] if i != "nan"]) if var_exists["awards_0_value_amount"] == True else None
    total_money_spent_currency = "ZAR"
    number_of_tenders = len(data)
    return ([{"number_of_tenders": number_of_tenders},
            {"unique_buyers": unique_buyers}, {"number_of_unique_buyers": number_of_unique_buyers},
            {"unique_sellers": unique_sellers}, {"number_of_unique_sellers": number_of_unique_sellers},
            {"total_money_spent": total_money_spent}, {"total_money_spent_currency": total_money_spent_currency}, {"total_money_spent": total_money_spent}])


#print(meta_variables(data_cleaned))



