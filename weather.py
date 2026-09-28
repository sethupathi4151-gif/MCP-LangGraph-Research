from fastmcp import FastMCP
import requests

mcp = FastMCP("Weather Server")


@mcp.tool
def get_weather(city: str) -> str:
    """Get the current weather for a city."""

    # Step 1: Find latitude and longitude
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"

    geo_params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    geo_response = requests.get(geo_url, params=geo_params)
    geo_data = geo_response.json()

    if "results" not in geo_data:
        return f"City not found: {city}"

    location = geo_data["results"][0]

    latitude = location["latitude"]
    longitude = location["longitude"]

    # Step 2: Get weather
    weather_url = "https://api.open-meteo.com/v1/forecast"

    weather_params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "timezone": "auto"
    }

    weather_response = requests.get(
        weather_url,
        params=weather_params
    )

    weather_data = weather_response.json()

    temperature = weather_data["current"]["temperature_2m"]
    wind_speed = weather_data["current"]["wind_speed_10m"]

    return (
        f"City: {city}\n"
        f"Temperature: {temperature} °C\n"
        f"Wind Speed: {wind_speed} km/h"
    )


if __name__ == "__main__":
    mcp.run()