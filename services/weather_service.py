import requests
from services.weather_utils import format_forecast_weather, format_current_weather

WEATHER_API_URI = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_API_URI = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "0e2ca89ed39d35cefc9a599038e33413"


def get_weather(city, unit):
    """
    Fetch current weather and 5-day forecast data.
    Returns a structured dictionary with 'current' and 'forecast'.
    """
    params = {"q": f"{city['name']},{city['country']}", "appid": API_KEY}
    current_weather = get_current_weather(params, unit)
    forecast = get_weather_forecast(params,unit)
        
    return {
        'current': current_weather,
        'forecast': forecast,
        'city': city['name']
    }

def get_current_weather(params, unit):
    # Fetch current weather
    weather_response = requests.get(WEATHER_API_URI, params)
    if weather_response.status_code != 200:
        return {"error": "Failed to fetch current weather data"}

    # Format weather into HTML readable form
    current_weather = format_current_weather(weather_response.json(), unit)
    return current_weather

def get_weather_forecast(params, unit):
    # Fetch weather forecast
    forecast_response = requests.get(FORECAST_API_URI, params)
    if forecast_response.status_code != 200:
        return {"error": "Failed to fetch weather forecast data"}

    # Format into 3 HTML readable entry
    forecast = format_forecast_weather(forecast_response.json(), unit)
    return forecast
