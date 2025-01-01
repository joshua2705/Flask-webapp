from flask import Blueprint, render_template, request, redirect, url_for
from services.calendar_service import save_events, get_events
from services.weather_service import get_weather_forecast
from services.weather_utils import select_image, find_forecast_weather, simplify_condition
from datetime import datetime, timedelta
from models.event import Event
import static.constants as constants
import pytz

API_KEY = constants.API_KEY
calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/calendar')
def calendar_page():
    events = [event for event in get_events() if is_future_event(event)]
    today = datetime.now(pytz.timezone('Europe/Paris')).date()
    date_range = [(today + timedelta(days=x)).strftime('%d-%m-%Y') 
                 for x in range(5)]
    day_range = [(today + timedelta(days=x)).strftime('%A') 
                 for x in range(5)]
    

    updated_events = []
    for event in events:
        params = {"q": f"{event.city},{event.country}", "appid": API_KEY}
        response_data = get_weather_forecast(params)
        
        forecast = find_forecast_weather(response_data, event.date)
        condition = simplify_condition(forecast['weather'][0]['main'])
        forecast_image_file = select_image(condition)
        
        updated_events.append((event,forecast_image_file))

    return render_template('calendar.html', 
                           events=updated_events, 
                           date_range=date_range, 
                           day_range=day_range, 
                           countries= constants.COUNTRIES
                           )

@calendar_bp.route('/calendar/add', methods=['POST'])
def add_event():
    events = [event for event in get_events() if is_future_event(event)]
    new_event = Event(
        name=request.form.get('title', 'Untitled Event'),
        date=request.form.get('date', datetime.now().strftime('%d-%m-%Y')),
        city=request.form.get('city', 'Unknown City'),
        country=request.form.get('country', 'Unknown Country'),
        description=request.form.get('description', 'No Description')
    )
    events.append(new_event)
    save_events(events)
    return redirect(url_for('calendar.calendar_page'))

def is_future_event(event):
    try:
        event_date = datetime.strptime(event.date, "%d-%m-%Y").date()
        return event_date >= datetime.now().date()
    except ValueError:
        return False
