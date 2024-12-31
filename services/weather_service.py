import requests
from services.weather_utils import format_forecast_weather, format_current_weather
import static.constants as constants

WEATHER_API_URI = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_API_URI = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "0e2ca89ed39d35cefc9a599038e33413"

countries = constants.COUNTRIES

def get_weather(city, unit):
    """
    Fetch current weather and 5-day forecast data.
    Returns a structured dictionary with 'current' and 'forecast'.
    """
    params = {"q": f"{city['name']},{city['country']}", "appid": API_KEY}
    current_weather = get_current_weather(params, unit)
    forecast = get_weather_forecast(params, unit)
        
    return {
        'current': current_weather,
        'forecast': forecast,
        'city': city['name'],
        'country': next((c['name'] for c in countries if c['code'] == city['country']), None)
    }

def get_current_weather(params, unit):
    # Fetch current weather
    weather_response = requests.get(WEATHER_API_URI, params)
    response_data = weather_response.json()

    # Validate the response
    if weather_response.status_code != 200 or 'main' not in response_data:
        return {
            'temp': 0,
            'condition': 'Unknown',
            'humidity': 0
        }

    # Format weather into an HTML-readable form
    current_weather = format_current_weather(response_data, unit)
    return current_weather

def get_weather_forecast(params, unit):
    # Fetch weather forecast
    forecast_response = requests.get(FORECAST_API_URI, params)
    response_data = forecast_response.json()

    # Validate the response
    if forecast_response.status_code != 200 or 'list' not in response_data:
        return [
            {'day': 'N/A', 'temp': 0, 'condition': 'Unknown'},
            {'day': 'N/A', 'temp': 0, 'condition': 'Unknown'},
            {'day': 'N/A', 'temp': 0, 'condition': 'Unknown'}
        ]

    # Format into 3 HTML-readable entries
    forecast = format_forecast_weather(response_data, unit)
    return forecast