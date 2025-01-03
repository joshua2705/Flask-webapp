from flask import Blueprint, render_template, request
from services.weather_service import get_weather
from services.weather_utils import select_image
import static.constants as constants

# Blueprint for weather routes
weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/', methods=['GET', 'POST'])
def weather_page():
    """
    Creates the weather page.

    Return: 
        Rendered HTML template ('weather.html') displaying:
        - Current weather data (temperature, condition, humidity).
        - A 3-day weather forecast.
        - The appropriate weather icon based on the current weather condition.
    """
    # Default to Paris, France for the initial display
    city = {"name": constants.DEFAULT_CITY, "country": constants.DEFAULT_COUNTRY}  
    unit = constants.DEFAULT_UNIT
    forecast_image_file = "images/default.png"
    forecast = None

    if request.method == 'POST':
        # Update city and country based on user input
        city['name'] = request.form.get('city', constants.DEFAULT_CITY)
        city['country'] = request.form.get('country', constants.DEFAULT_COUNTRY)

    # Fetch weather data for the provided city and country
    forecast = get_weather(city, unit)

    if not forecast or 'current' not in forecast:
        # Handle errors or missing data with default values
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

    # Select the appropriate weather icon based on the current condition
    forecast_image_file = select_image(forecast['current']['condition'])

    # Render the weather page with forecast details and selected image
    return render_template('weather.html', countries=constants.COUNTRIES, forecast=forecast, image_file=forecast_image_file)
