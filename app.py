from flask import Flask, request, jsonify
import json
from get_data import get_data
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Home Page!'

@app.route('/about')
def about():
    return 'This is the About Page.'


@app.route('/get_weather', methods=['POST'])
def  get_weather():
    # Check if the request contains JSON data
    if request.is_json:
        data = request.get_json()  # Get the JSON data from the request
        # Process the JSON data (you can loop through it or do other operations)
        id_lat_lon_data = []
        for entry in data:
            id_lat_lon_data.append({
                "id": entry['id'],
                "lat": entry['lat'],
                "lon": entry["lon"]                
            })

        data = get_data(id_lat_lon_data)
        return jsonify(data), 200
        
    else:
        return jsonify({"message": "Invalid data format, expecting JSON", "status": "error"}), 400


if __name__ == '__main__':
    app.run(debug=True)
