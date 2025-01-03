from flask import Blueprint, render_template, request, redirect, url_for
from services.calendar_service import save_events, get_events
from services.weather_service import get_weather_forecast
from services.weather_utils import select_image, find_forecast_weather, simplify_condition
from datetime import datetime, timedelta
from models.event import Event
import static.constants as constants
import pytz

# API key for weather service
API_KEY = constants.API_KEY

# Create Flask blueprint for the calendar
calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/calendar')
def calendar_page():
    """ 
    The calendar_page function returns the calendar page with updated events and weather information.

    Returns:
        Rendered HTML for the calendar page with the event list, date range, day range, and countries.
    """
    # Fetch future events only
    events = [event for event in get_events() if is_future_event(event)]

    # Get today's date in Paris timezone and generate the next 5 days' date and weekday names
    today = datetime.now(pytz.timezone('Europe/Paris')).date()
    date_range = [(today + timedelta(days=x)).strftime('%d-%m-%Y') for x in range(5)]
    day_range = [(today + timedelta(days=x)).strftime('%A') for x in range(5)]

    # Update events with weather forecasts and images
    updated_events = []
    for event in events:
        params = {"q": f"{event.city},{event.country}", "appid": API_KEY}
        response_data = get_weather_forecast(params)
        forecast = find_forecast_weather(response_data, event.date)
        condition = simplify_condition(forecast['weather'][0]['main'])
        forecast_image_file = select_image(condition)
        updated_events.append((event, forecast_image_file))

    return render_template('calendar.html', 
                           events=updated_events, 
                           date_range=date_range, 
                           day_range=day_range, 
                           countries=constants.COUNTRIES)

@calendar_bp.route('/calendar/add', methods=['POST'])
def add_event():
    """
    Adds a new event to the calendar and redirects back to the calendar page.

    Returns:
        Redirects to the calendar page after the event is saved.
    """
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
    """
    Determines whether an event is today or in the future.

    Arguments:
        event (Event): The event to check, containing a date attribute in "%d-%m-%Y" format.

    Returns:
        bool: True if the event is today or in the future, False otherwise.
    """
    try:
        event_date = datetime.strptime(event.date, "%d-%m-%Y").date()
        return event_date >= datetime.now().date()
    except ValueError:
        return False
