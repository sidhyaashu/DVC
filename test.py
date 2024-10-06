import pandas as pd

Data =[
    {"name":"Asutosh sidhya","age":20,"city":"Kolkata"},
    {"name":"Rama sidhya","age":21,"city":"local"},
    {"name":"Signal sidhya","age":22,"city":"pak"},
]





Data = pd.DataFrame(Data)
Data.to_csv("data/data.csv",index=False)