from datetime import datetime
from timezonefinder import TimezoneFinder # type: ignore
from geopy.geocoders import Nominatim # type: ignore
import requests




def get_location_info(lat, lon):
    """Fetch location information from coordinates using reverse geocoding."""
    geolocator = Nominatim(user_agent="coordinate_info_fetcher")
    location = geolocator.reverse((lat, lon), exactly_one=True)
    return location.address if location else "Location information not found."

def get_timezone(lat, lon):
    """Fetch the timezone of a location using the coordinates."""
    tf = TimezoneFinder()
    timezone = tf.timezone_at(lat=lat, lng=lon)
    if timezone:
        current_time = datetime.now().astimezone().strftime('%Y-%m-%d %H:%M:%S')
        return timezone, current_time
    return "Timezone not found", "N/A"

API_KEY = "0c758ca721cd9b32889afae0cce03927"

def get_weather(lat, lon):
    """Fetch the current weather information using OpenWeatherMap API."""
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            weather = data.get("weather", [{}])[0].get("description", "N/A")
            temperature = data.get("main", {}).get("temp", "N/A")
            return f"{weather.capitalize()}, {temperature}°C"
        return "Weather information not available"
    except Exception as e:
        return f"Error fetching weather: {str(e)}"



