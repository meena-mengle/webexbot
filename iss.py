import requests
from datetime import datetime

# Mapbox API Key
MAPBOX_API_KEY = 'pk.eyJ1IjoibTMzbmEiLCJhIjoiY21iNTdzazVvMXl0ZjJpc2I5YzI4aTIwaCJ9.X8TJe6IPT0NqbtWN0_I6jQ'

# N2YO API Key (replace with your key)
N2YO_API_KEY = 'HRXYT7-F6LQK3-C7F2FU-5HNL'

def get_coordinates(city_name):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{city_name}.json"
    params = {
        'access_token': MAPBOX_API_KEY,
        'limit': 1
    }
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200 and data['features']:
        coordinates = data['features'][0]['geometry']['coordinates']
        print(f"\n{city_name} Coordinates:")
        print(f"Longitude: {coordinates[0]}")
        print(f"Latitude: {coordinates[1]}")
        return coordinates  # returns [longitude, latitude]
    else:
        print(f"Error: Could not find coordinates for '{city_name}'")
        return None

def get_iss_pass_n2yo(latitude, longitude):
    satellite_id = 25544  # ISS
    observer_alt = 0  # Assume sea level
    days = 1
    min_visibility = 1

    url = f"https://api.n2yo.com/rest/v1/satellite/visualpasses/{satellite_id}/{latitude}/{longitude}/{observer_alt}/{days}/{min_visibility}/&apiKey={N2YO_API_KEY}"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200 and 'passes' in data:
            if not data['passes']:
                print("\nNo visible ISS passes in the next day.")
                return

            print("\nUpcoming ISS visible passes (from N2YO):")
            for p in data['passes']:
                start_time = datetime.fromtimestamp(p['startUTC'])
                duration = p['duration']
                print(f"- Starts: {start_time} | Duration: {duration} seconds")
        else:
            print("\nNo pass data found or API limit reached.")
    except requests.RequestException as e:
        print(f"N2YO API request failed: {e}")

# Example usage
city = input("Enter a city name: ")
coordinates = get_coordinates(city)
if coordinates:
    lon, lat = coordinates  # Mapbox gives [lon, lat]
    get_iss_pass_n2yo(lat, lon)
