from flask import Blueprint, render_template, request, redirect, url_for
from services.calendar_service import save_events, get_events
from datetime import datetime, timedelta
from models.event import Event
import pytz

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/calendar')
def calendar_page():
    events = get_events()
    events = list(filter(past_events, events))
    today = datetime.now(pytz.timezone('Europe/Paris')).date()
    date_range = [(today + timedelta(days=x)).strftime('%d-%m-%Y') 
                 for x in range(5)]
    day_range = [(today + timedelta(days=x)).strftime('%A') 
                 for x in range(5)]
    return render_template('calendar.html', events=events, date_range=date_range, day_range=day_range)

@calendar_bp.route('/calendar/add', methods=['POST'])
def add_calendar_event():

    events = get_events()
    events = list(filter(past_events, events))
    new_event = Event(
        name=request.form['title'],
        date=request.form['date'],
        city=request.form['city'],
        country=request.form['country'],
        description=request.form['description']
    )
    
    events.append(new_event)
    save_events(events)
    return redirect(url_for('calendar.calendar_page'))

def past_events(event):
    today = datetime.strptime(event.date, "%d-%m-%Y").date()
    return today >= datetime.now().date()