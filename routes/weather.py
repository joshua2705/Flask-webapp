from flask import Blueprint, render_template
from services.weather_service import get_weather_forecast

weather_bp = Blueprint('weather', __name__)

@weather_bp.route('/')
def weather_page():
    forecast = get_weather_forecast()
    return render_template('weather.html', forecast=forecast)