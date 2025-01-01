import requests
from services.weather_utils import format_forecast_weather, format_current_weather
import static.constants as constants

WEATHER_API_URI = constants.WEATHER_API_URI
FORECAST_API_URI = constants.FORECAST_API_URI
API_KEY = constants.API_KEY
countries = constants.COUNTRIES

def get_weather(city, unit):
    """
    Fetch current weather and 5-day forecast data.
    Returns a structured dictionary with 'current' and 'forecast'.
    """
    params = {"q": f"{city['name']},{city['country']}", "appid": API_KEY}
    current_weather = format_current_weather(get_current_weather(params), unit)
    forecast        = format_forecast_weather(get_weather_forecast(params), unit)
        
    return {
        'current': current_weather,
        'forecast': forecast,
        'city': city['name'],
        'country': next((country['name'] for country in countries if country['code'] == city['country']), None)
    }

def get_current_weather(params):
    # Fetch current weather
    weather_response = requests.get(WEATHER_API_URI, params)
    response_data = weather_response.json()

    # Validate the response
    if weather_response.status_code != 200 or 'main' not in response_data:
        return {
            "main":{
                'temp': 0,
                'condition': 'Unknown',
                'humidity': 0
            },
            "weather": [
                {
                    "main": "Null",
                }
            ],
        } 
    return response_data

def get_weather_forecast(params):
    # Fetch weather forecast
    forecast_response = requests.get(FORECAST_API_URI, params)
    response_data = forecast_response.json()

    # Validate the response
    if forecast_response.status_code != 200 or 'list' not in response_data:
        return {
                "list": [{  "main": {"temp": 273,},
                            "weather": [{"main": "Null"}],
                            "dt_txt": "2000-01-01 00:00:00"
                        }]
                }
    return response_data
