from flask import Flask, request, jsonify
import json
from get_data import get_data
app = Flask(__name__)

@app.route('/get_weather', methods=['POST'])
def  get_weather():
    if request.is_json:
        data = request.get_json() 
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
        return jsonify({"message": "Kiểu dữ liệu sai, phải là JSON", "status": "error"}), 400


if __name__ == '__main__':
    app.run(debug=True)
