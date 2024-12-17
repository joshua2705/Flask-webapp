#from flask import Blueprint, render_template
#from services.weather_service import get_weather_forecast

#weather_bp = Blueprint('weather', __name__)

#@weather_bp.route('/')
#def weather_page():
 #   forecast = get_weather_forecast()
  #  return render_template('weather.html', forecast=forecast)
from flask import Blueprint, render_template, request
from services.weather_service import get_weather_forecast

# Blueprint for weather routes
weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/', methods=['GET', 'POST'])
def weather_page():
    if request.method == 'POST':
        # Retrieve city name from the form input
        city = request.form.get('city')

        print(city)
        # Call the weather forecast function with the entered city
        forecast = get_weather_forecast(city)
        if not forecast or 'current' not in forecast:
            forecast = {
                'current': {'temp': 0, 'condition': 'Unknown', 'humidity': 0},
                'forecast': [
                    {'day': 'N/A', 'temp': 0, 'condition': 'Unknown'},
                    {'day': 'N/A', 'temp': 0, 'condition': 'Unknown'},
                    {'day': 'N/A', 'temp': 0, 'condition': 'Unknown'}
                ]
            }
    
    # Render the template with the forecast and city name
    return render_template('weather.html', forecast=forecast, city=city)
