import requests
import csv
from datetime import datetime, timedelta
import json
from flask import jsonify

API_KEY = "CUQGXXL634ZX52TA4FRSUS99Y"


def F_to_C(F):
    return (F-32)*5/9

def inch_to_mm(inch):
    return inch*25.4

def cal_chance(precip, precip_prob):
    return  inch_to_mm(precip)*precip_prob/100

def get_data(id_lat_lon):
    response_dict = {}

    for e in id_lat_lon:
        id, lat, lon = e["id"], e["lat"], e["lon"]
        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}/last3days/next3days?key={API_KEY}"
        response_dict[id] = []
        response = requests.get(url)
        # Check if the request was successful
        if response.status_code == 200:
            # Print the response content (JSON in this case)
            data = response.json()  # Convert the response to JSON
            days_data = data["days"]
            
            for day_data in days_data:
                if day_data["preciptype"] != None and "rain" in day_data["preciptype"]:
                    chance = cal_chance(day_data["precip"], day_data["precipprob"]) 
                else:
                    chance = 0
                    
                response_dict[id].append({
                    "date": day_data["datetime"],
                    "temperature": F_to_C(day_data["temp"]),
                    "chance": chance
                    
                })
        
        else:
            print(f"Failed to retrieve data. Status code: {response.status_code}")

    return response_dict



    



