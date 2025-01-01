from flask import Blueprint, render_template, request, redirect, url_for
from services.calendar_service import save_events, get_events
from datetime import datetime, timedelta
from models.event import Event
import static.constants
import pytz

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/calendar')
def calendar_page():
    events = [event for event in get_events() if is_future_event(event)]
    #events = list(filter(past_events, events))
    today = datetime.now(pytz.timezone('Europe/Paris')).date()
    date_range = [(today + timedelta(days=x)).strftime('%d-%m-%Y') 
                 for x in range(5)]
    day_range = [(today + timedelta(days=x)).strftime('%A') 
                 for x in range(5)]
    return render_template('calendar.html', events=events, date_range=date_range, day_range=day_range, countries= static.constants.COUNTRIES)

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
