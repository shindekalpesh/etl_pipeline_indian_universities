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
    print(">> API_URL", type(API_URL), API_URL)
    print(">> data", type(data), data)
    
except:
    print("Error occured while fetching the API url! ")

