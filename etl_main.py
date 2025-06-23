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

column_check_state_province = df['state-province'].value_counts()

# print(type(column_check_state_province), "\n", column_check_state_province)

z = df[df['state-province']=='Mumbai']

# print(z)

indian_states = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", 
                 "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", 
                 "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", 
                 "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]

# print(">> check check", df['state-province'].to_list())

state = []
city = []

for i in df['state-province'].to_list():
    # print(i)
    if i in indian_states:
        # print(f"{i} is a state!")
        # df['state'] = i
        state.append(i)
        city.append("NA")
    else:
        # print(f"{i} is a city!")
        # df['city'] = i
        state.append("NA")
        city.append(i)
        
df['state'] = state
df['city'] = city

# print(">> df.head(15)", "\n", df.head(15))

# As of now, worked on 'state-province' column to separate 'state' and 'city' columns.
# More operations can be performed on this part. Time being moving ahead.

# df['domains'] = df['domains'].astype(str).str.strip('[]')
# df['web_pages'] = df['web_pages'].astype(str).str.strip('[]')

df['domains'] = df['domains'].astype(str).str.replace('[', '', regex=False).str.replace(']', '', regex=False).str.replace("'", '', regex=False)
df['web_pages'] = df['web_pages'].astype(str).str.replace('[', '', regex=False).str.replace(']', '', regex=False).str.replace("'", '', regex=False)

print(">> df.head(15)", "\n", df.head(15))



