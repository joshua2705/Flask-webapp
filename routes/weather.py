from flask import Blueprint, render_template, request
from services.weather_service import get_weather
from services.weather_utils import select_image
import static.constants as constants

# Blueprint for weather routes
weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/', methods=['GET', 'POST'])
def weather_page():
    # Default city: Paris, France
    city = constants.DEFAULT_CITY
    
    # Default unit: Celsius
    unit = constants.DEFAULT_UNIT
    forecast_image_file = "images/default.png"
    forecast = None

    if request.method == 'POST':
        # Retrieve city name from the form input
        city['name'] = request.form.get('city')

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
    return render_template('weather.html', forecast=forecast, image_file = forecast_image_file)
    
