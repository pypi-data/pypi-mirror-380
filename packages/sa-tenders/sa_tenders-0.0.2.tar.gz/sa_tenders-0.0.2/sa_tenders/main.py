'''
programmer; ntuthuko hlela
goal; scrape sa etenders data
'''
'''
Deploying: 
twine upload dist/*
'''
import flatdict

import dict_to_dataframe
import data_cleaning
import adding_variables



class sa_tenders():

    def __init__(self, page_number: int=1, page_size:int=10, start_date:str="2020-01-01", end_date:str="2024-12-31", currently_advertised=True, awarded=True, *args, **kwargs):

        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.end_date = end_date
        self.currently_advertised = currently_advertised
        self.awarded = awarded


        print("Fetching data...", end=" ")
        raw_data_frame = dict_to_dataframe.dict_to_dataframe(self.page_number, self.page_size, self.start_date, self.end_date, self.currently_advertised, self.awarded)
        print("Done.")

        self.meta_data = raw_data_frame["meta_data"]
        self.raw_data_dict = raw_data_frame["raw_data"]
        self.cleaned_dataframe = data_cleaning.data_cleaning(raw_data_frame["full_data_dataframe"])
        self.meta_data.extend(adding_variables.meta_variables(self.cleaned_dataframe))
        meta_temp2 = {}

        for i in self.meta_data:
            key = (list(i.keys()))[0]
            value = (list(i.values()))[0]
            meta_temp2[str(key)] = value


        self.meta_data = meta_temp2

sa_tenders()