from flask import Blueprint, render_template, request, redirect, url_for
from services.calendar_service import save_events, get_events
from datetime import datetime
import calendar
from models.event import Event

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/calendar')
def calendar_page():
    events = get_events()
    events = list(filter(past_events, events))
    for event in events:
        event.date = datetime.strptime(event.date, "%Y-%m-%d").strftime("%A")
    print(events)
    return render_template('calendar.html', events=events)

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
    event_date = datetime.strptime(event.date, "%Y-%m-%d").date()
    return event_date >= datetime.now().date()