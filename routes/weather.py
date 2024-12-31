from flask import Blueprint, render_template, request
from services.weather_service import get_weather
import static.constants as constants

# Blueprint for weather routes
weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/', methods=['GET', 'POST'])
def weather_page():
    # Default to Paris, France
    city = {"name": constants.DEFAULT_CITY, "country": constants.DEFAULT_COUNTRY}  
    unit = constants.DEFAULT_UNIT

    if request.method == 'POST':
        # Retrieve city and country from form
        city['name'] = request.form.get('city', constants.DEFAULT_CITY)
        city['country'] = request.form.get('country', constants.DEFAULT_COUNTRY)

    # Fetch weather data
    forecast = get_weather(city, unit)
    
    # Pass data to template
    return render_template('weather.html',countries=constants.COUNTRIES,forecast=forecast)