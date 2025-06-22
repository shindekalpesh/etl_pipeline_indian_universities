import requests
import pandas as pd
# from sqlalchemy import create_engine

# def extract()-> dict:
#     """Extract:
#     Extracts data from API.
#     Returns:
#         dict: Returns dictionary
#     """
    
#     API_URL = "http://universities.hipolabs.com/search?country=United+States"
#     data = requests.get(API_URL).json()
    
#     return data

try:
    API_URL = "http://universities.hipolabs.com/search?country=India"
    data = requests.get(API_URL).json()
    # print(">> API_URL", type(API_URL), API_URL)
    # print(">> data", type(data), data)
    
except:
    print("Error occured while fetching the API url! ")

df = pd.DataFrame(data)
print(">> df.head()", "\n", df.head())
print(">> df.shape", "\n", df.shape)
print(">> df.info()", "\n", df.info())

print("Unique entries from 'country' column:", "\n", df['country'].unique())
# It is confirmed that the data only consists of 'country': 'India'. Hence removing the country column since it makes no value addition.
print("Columns before dropping 'country' column: ", "\n", df.columns.to_list())
df = df.drop(columns='country')
print("Columns after dropping 'country' column: ", "\n", df.columns.to_list())


print("Unique entries from 'alpha_two_code' column:", "\n", df['alpha_two_code'].unique())
# It is confirmed that the data only consists of 'alpha_two_code': 'IN'. Hence removing the country column since it makes no value addition.
print("Columns before dropping 'alpha_two_code' column: ", "\n", df.columns.to_list())
df = df.drop(columns='alpha_two_code')
print("Columns after dropping 'alpha_two_code' column: ", "\n", df.columns.to_list())
