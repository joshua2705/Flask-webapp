from flask import Blueprint, render_template
from services.weather_service import get_weather

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/')
def weather_page():
    # Default city: Paris, France
    city = {'name': 'Paris', 'country': 'FR'}  # Hardcoded default city
    
    # Default unit: Celsius
    unit = 'C'
    
    # Fetch weather data
    forecast = get_weather(city, unit=unit)
    
    if forecast:
        return render_template('weather.html', forecast=forecast)
    else:
        return "Failed to fetch weather data", 500
