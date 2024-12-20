import requests
import pycountry

WEATHER_API_URI = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_API_URI = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "0e2ca89ed39d35cefc9a599038e33413"  # Replace with your actual API key


def get_country_name(country_code):
    """Convert a country code (e.g., 'GB') to its full name (e.g., 'United Kingdom')."""
    try:
        return pycountry.countries.get(alpha_2=country_code).name
    except AttributeError:
        return country_code


def get_weather_forecast(city, unit='C'):
    """
    Fetch current weather and 5-day forecast data.
    Returns a structured dictionary with 'current' and 'forecast'.
    """
    # Fetch current weather
    weather_response = requests.get(
        WEATHER_API_URI, params={"q": f"{city['name']},{city['country']}", "appid": API_KEY}
    )
    current_data = weather_response.json()

    # Fetch 5-day forecast
    forecast_response = requests.get(
        FORECAST_API_URI, params={"q": f"{city['name']},{city['country']}", "appid": API_KEY}
    )
    forecast_data = forecast_response.json()

    # Check for errors
    if weather_response.status_code != 200 or forecast_response.status_code != 200:
        print("Error fetching weather data.")
        return None

    # Temperature unit conversion
    def kelvin_to_unit(kelvin):
        return (kelvin - 273.15) if unit == 'C' else (kelvin - 273.15) * 1.8 + 32

    unit_label = "°C" if unit == 'C' else "°F"

    # Function to generalize weather conditions
    def simplify_condition(description):
        description = description.lower()
        if description in ["few clouds", "scattered clouds", "broken clouds", "overcast clouds"]:
            return "Cloudy"
        elif description in ["shower rain", "rain"]:
            return "Rain"
        elif description in ["mist", "haze"]:
            return "Mist"
        return description.capitalize()  # Default condition

    # Current weather
    current_weather = {
        'temp': round(kelvin_to_unit(current_data['main']['temp'])),
        'condition': simplify_condition(current_data['weather'][0]['description']),
        'humidity': current_data['main']['humidity'],
        'unit': unit_label
    }

    # Simplified forecast: picking every 8th data point (roughly one per day)
    forecast = []
    for i in range(0, len(forecast_data['list']), 8):  # Each data point is 3 hours apart
        day_data = forecast_data['list'][i]
        forecast.append({
            'day': day_data['dt_txt'].split()[0],  # Extract date
            'temp': round(kelvin_to_unit(day_data['main']['temp'])),
            'condition': simplify_condition(day_data['weather'][0]['description'])
        })
        
    return {
        'current': current_weather,
        'forecast': forecast
    }
