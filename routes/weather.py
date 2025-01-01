from flask import Blueprint, render_template, request
from services.weather_service import get_weather
from services.weather_utils import select_image
import static.constants as constants

# Blueprint for weather routes
weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/', methods=['GET', 'POST'])
def weather_page():
    # Default to Paris, France
    city = {"name": constants.DEFAULT_CITY, "country": constants.DEFAULT_COUNTRY}  
    unit = constants.DEFAULT_UNIT
    forecast_image_file = "images/default.png"
    forecast = None

    if request.method == 'POST':
        # Retrieve city and country from form
        city['name'] = request.form.get('city', constants.DEFAULT_CITY)
        city['country'] = request.form.get('country', constants.DEFAULT_COUNTRY)

    # Fetch weather data
    forecast = get_weather(city, unit)

    #Error handling
    if not forecast or 'current' not in forecast:
        forecast = {
                'current': {'temp': 0, 'condition': 'Unknown', 'humidity': 0},
                'forecast': [
                    {'day': 'N/A', 'temp': 0, 'condition': 'Unknown'},
                    {'day': 'N/A', 'temp': 0, 'condition': 'Unknown'},
                    {'day': 'N/A', 'temp': 0, 'condition': 'Unknown'}
                ],
                'city': 'N/A',
                'country': ''
            }

    forecast_image_file = select_image(forecast['current']['condition'])
    return render_template('weather.html', countries=constants.COUNTRIES, forecast=forecast, image_file = forecast_image_file)
    
