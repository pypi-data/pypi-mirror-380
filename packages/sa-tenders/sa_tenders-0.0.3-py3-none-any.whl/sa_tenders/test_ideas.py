'''
Programmer: Ntuthuko Hlela
The goal of this script is to test ideas
'''


import pandas as pd
import requests
from operator import itemgetter
import numpy as np

'''
def args_test(*args):
    o = sum(args)
    print(o)

args_test(1,2,3)

def kwargs_test(**kwargs):
    for i in kwargs.keys():
        print(i)

kwargs_test(a=1,b=2,c=3,d=4)


g = "https://ocds-api.etenders.gov.za/api/OCDSReleases/release/ocds-9t57fa-118250"
f = requests.get(g)
print(f.status_code)


class x():
    def __init__(self, *args, **kwargs):
        self.value = "global"
        self.calc = 1

    def y(self):
        self.u = "func y"
        self.calc2 = 1 + self.calc
        print(self.calc2)

    def z(self):
        print(self.calc)

x = x().z()
print(x)


x =  [{"name":"John", "age":12, "city": "jhb"},
                  {"name":"Axe", "age":22, "city": "cpt"},
                  {"name":"Goerge", "age":31, "city": "cpt"},
      {"name":"", "age":31, "city": "cpt"}]

c = [i["name"] or None for i   in x]
print(c)

import numpy as np
z = pd.DataFrame(columns=["age", "city", "company" ])
z.loc[len(z)] = [5, "jhb", "jpal"]
z.loc[len(z)] = [6, "cpt", "datafirst"]
print(z.head())
'''


'''
f = final_data(dict1)
h = []
for i in f:
    h.append(i[0])

u = (pd.DataFrame(f)).T
z = u.set_axis(h, axis=1)
z.drop(0, inplace=True, axis=0)
print(z)





l = [1,2,3,4,5, 1, 2]

for i in l:
    if i > 2:
        continue
    else:
        print(i)

print("broke")



for i in l:
    if i > 2:
        break
    else:
        print(i)

print("broke")


p = [1,2,3,3]
c = []
for i in p:
    if i not in c:
        c.append(i)
        print(i)
    elif i in c:
        print("dup:", i)


l = pd.DataFrame([[1,2,3,4,4,5], [1,2,3,4,5,5], [1,2,3,4,5]])

x = l.astype(str)
print(x.dtypes)



g = " Ntuthuko "

l = np.array([1,2,3,200, 4,4,5, 100])
x = np.where((l>1) & (l<10), True, False)
print(x)


m = ["1", "kk"]
m.remove("kk")
print(m)


try:
    h = 1+ 1
    s = 1+"2"
except Exception as e:
    print(e)
    

x = [["datafirst", 100, 1], ["jpal", 200,1], ["saldru", 300,1], ["dna", 400,1], ["jpal", 500,1], ["saldru", 600,1], ["dna", 700,1], ["datafirst", 100,2]]
df = pd.DataFrame(x, columns=["name", "amount", "val"])
df["total_expenditure"] = df.groupby("name")["amount"].transform("sum")
print(df.groupby(["name", "val"]).transform("sum"))
print(df)


l = [1,2,3,200, 4,4,5, 100, 1,1,1,1]
print(sum(l))

x = [{"name": 1, "amount": 100}, {"name": 2, "amount": "2"}]
for i in x:
    print(list(i.keys()))
'''

from sa_tenders import sa_tenders
source = sa_tenders(page_size=100, start_date="2024-01-01", end_date="2024-12-31")
meta_data = source.meta_data
raw_data = source.raw_data_dict
clean_data = source.cleaned_dataframe

for i in [meta_data, raw_data, clean_data]:
    print(i)

clean_data.to_excel("sa_tenders_data.xlsx")