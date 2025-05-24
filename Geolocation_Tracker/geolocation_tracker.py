import requests
import folium
print("Script started")  # Add this line at the top


# Fetch geolocation data based on IP
def get_geolocation():
    try:
        # Using ip-api.com, which doesn't require an API key
        response = requests.get('http://ip-api.com/json/')
        response.raise_for_status()
        data = response.json()
        lat = data['lat']
        lon = data['lon']
        city = data.get('city', 'Unknown')
        country = data.get('country', 'Unknown')
        return lat, lon, city, country
    except requests.RequestException as e:
        print(f"Error fetching geolocation data: {e}")
        return None

# Generate and save the map
def create_map(lat, lon, city, country):
    # Create a map centered at the user's location
    user_map = folium.Map(location=[lat, lon], zoom_start=13)

    # Add a marker with location info
    folium.Marker(
        [lat, lon],
        popup=f"Location: {city}, {country}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(user_map)

    # Save the map to an HTML file
    map_filename = 'user_location_map.html'
    user_map.save(map_filename)
    print(f"Map has been saved to {map_filename}")

# Main execution
if __name__ == "__main__":
    geolocation = get_geolocation()
    if geolocation:
        lat, lon, city, country = geolocation
        print(f"Your approximate location: {city}, {country} ({lat}, {lon})")
        create_map(lat, lon, city, country)
    else:
        print("Could not retrieve geolocation data.")
