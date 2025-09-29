'''
Programmer: Ntuthuko Hlela
Date created: 2025/09/14
Goal: Cleaning the pull data
Contraints / priotirize: This should run at scale.
'''


import pandas as pd
import numpy as np
import flatdict
import re
import dict_to_dataframe

def data_cleaning(dataframe):

    # Removing columns that are class flatdict.FlatterDict
    for i in dataframe.columns:
        datatype = [type(j) for j in dataframe[i]]
        flatdict_type_counter = datatype.count(flatdict.FlatterDict)
        if flatdict_type_counter > 0:
            dataframe.drop(i, axis=1, inplace=True)


    # Dealing with empty cells
    dataframe = dataframe.astype(str)
    dataframe = dataframe.map(lambda x: x.strip())
    dataframe.where((dataframe!="") & (dataframe!="-"), "nan", inplace=True)

    return dataframe

#data = (dict_to_dataframe.dict_to_dataframe(page_size=50))["full_data_dataframe"]
#data_cleaning(data)




