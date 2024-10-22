from flask import Flask, jsonify
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import os

app = Flask(__name__)
geolocator = Nominatim(user_agent="geoapiExercises")

@app.route('/pin/<postal_code>', methods=['GET'])
def get_location_info(postal_code):
    try:
        location = geolocator.geocode(postal_code)
        if location:
            return jsonify({
                'postal_code': postal_code,
                'location_name': location.address,
                'latitude': location.latitude,
                'longitude': location.longitude
            })
        else:
            return jsonify({'error': 'Location not found'}), 404
    except GeocoderTimedOut:
        return jsonify({'error': 'Geocoder service timed out'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5018))
    app.run(host='0.0.0.0', port=port, debug=True)