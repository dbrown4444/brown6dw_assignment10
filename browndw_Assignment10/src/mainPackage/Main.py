# David Brown and John Cannon
# brown6dw@mail.uc.edu"
# Assignment 10"
# 11/09/2023
# IS 4010
# Fall 2023
# This project shows we can use API's correctly and search for data in them.


import requests
import json

# Set your API key
X_RapidAPI_Key = "781ef28139msh08cd5546fa77130p165ed3jsn4a2e29c2bd15"

# Set the request parameters
params = {
    "id": "4360644"
}

# Set the headers
headers = {
    "X-RapidAPI-Key": X_RapidAPI_Key,
    "Content-Type": "application/json"
}

# Build the URL
url = "https://nfl-api-data.p.rapidapi.com/nfl-player-info/v1/data"

# Send the GET request
response = requests.get(url, params=params, headers=headers)

# Check the response status code
if response.status_code == 200:
    # Try parsing the JSON response
    try:
        data = response.json()
    except json.decoder.JSONDecodeError:
        print("Invalid JSON response received.")
        exit()

#  Checking to see what keys my Data contains

data = {'id': 'age', 'jersey': 12345}

try:
    data = response.json()
except json.decoder.JSONDecodeError:
    print("Invalid JSON response received.")
    exit()

# Check if the data dictionary contains keys
if data.keys():
    print("The data dictionary contains keys.")

# Process the data
age = data['age']
jersey = data['jersey']

# Print the player information
print(f"Age: {age}")
print(f"Jersey: {jersey}")



