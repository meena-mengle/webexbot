import requests

# Replace this with your Mapbox API key
MAPBOX_API_KEY = 'pk.eyJ1IjoibTMzbmEiLCJhIjoiY21iNTdzazVvMXl0ZjJpc2I5YzI4aTIwaCJ9.X8TJe6IPT0NqbtWN0_I6jQ'

def get_coordinates(city_name):
    url = f"https://api.mapbox.com/geocoding/v5/mapbox.places/{city_name}.json"
    params = {
        'access_token': MAPBOX_API_KEY,
        'limit': 1
    }
    response = requests.get(url, params=params)
    print(response)
    data = response.json()

    if response.status_code == 200 and data['features']:
        coordinates = data['features'][0]['geometry']['coordinates']
        print(f"{city_name} Coordinates:")
        print(f"Longitude: {coordinates[0]}")
        print(f"Latitude: {coordinates[1]}")
        return coordinates
    else:
        print(f"Error: Could not find coordinates for '{city_name}'")
        return None

# Example usage
city = input("Enter a city name: ")
get_coordinates(city)
