'''
programmer; ntuthuko hlela
goal; scrape sa etenders data
'''
'''
Deploying: 
python setup.py sdist bdist_wheel
twine upload dist/*
'''
import flatdict
from .dict_to_dataframe import dict_to_dataframe
from .data_cleaning import data_cleaning
from .adding_variables import meta_variables



class sa_tenders():


    def __init__(self, page_number: int=1, page_size:int=10, start_date:str="2020-01-01", end_date:str="2024-12-31", *args, **kwargs):

        self.page_number = page_number
        self.page_size = page_size
        self.start_date = start_date
        self.end_date = end_date


        print("Fetching data...", end=" ")
        raw_data_frame = dict_to_dataframe(self.page_number, self.page_size, self.start_date, self.end_date)
        print("Done.")

        self.meta_data = raw_data_frame["meta_data"]
        self.raw_data_dict = raw_data_frame["raw_data"]
        self.cleaned_dataframe = data_cleaning(raw_data_frame["full_data_dataframe"])
        self.meta_data.extend(meta_variables(self.cleaned_dataframe))
        meta_temp2 = {}

        for i in self.meta_data:
            key = (list(i.keys()))[0]
            value = (list(i.values()))[0]
            meta_temp2[str(key)] = value


        self.meta_data = meta_temp2


