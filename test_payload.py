import requests
import json

# Define the URL for the API
url = 'http://127.0.0.1:5000/data'

# Load the JSON file into a variable
with open('data.json') as f:
    json_data = json.load(f)

# Send the POST request with the loaded JSON data
response = requests.post(url, json=json_data)

# Print the response from the server
print(response.json())
