import requests

print("Weather App")

city = input("Enter city name: ")

try:
    # Find city location
    location_url = "https://geocoding-api.open-meteo.com/v1/search"
    location_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    location_response = requests.get(location_url, params=location_params)
    location_data = location_response.json()

    if "results" not in location_data:
        print("City not found.")
    else:
        latitude = location_data["results"][0]["latitude"]
        longitude = location_data["results"][0]["longitude"]
        city_name = location_data["results"][0]["name"]

        # Get weather
        weather_url = "https://api.open-meteo.com/v1/forecast"
        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "timezone": "auto"
        }

        weather_response = requests.get(weather_url, params=weather_params)
        weather_data = weather_response.json()

        current = weather_data["current"]

        print("\nWeather Details")
        print("City:", city_name)
        print("Temperature:", current["temperature_2m"], "°C")
        print("Humidity:", current["relative_humidity_2m"], "%")
        print("Wind Speed:", current["wind_speed_10m"], "km/h")

except Exception:
    print("Unable to get weather information.")