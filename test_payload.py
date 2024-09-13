import requests
import json


url = 'http://127.0.0.1:5000/get_weather'
with open('data.json') as f:
    json_data = json.load(f)
response = requests.post(url, json=json_data)
print(response.json())
