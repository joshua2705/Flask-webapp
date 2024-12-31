from flask import Blueprint, render_template, request, redirect, url_for
from services.calendar_service import save_events, get_events
from datetime import datetime
from models.event import Event

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/calendar')
def calendar_page():
    events = get_events()
    events = [event for event in events if is_future_event(event)]
    date_format_map = {event.date: datetime.strptime(event.date, "%Y-%m-%d").strftime("%A") for event in events}
    
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logging.debug(events)
    print(events)
    
    return render_template('calendar.html', events=events)

@calendar_bp.route('/calendar', methods=['POST'])
def add_event():
    events = get_events()
    new_event = Event(
        name=request.form.get('title', 'Untitled Event'),
        date=request.form.get('date', datetime.now().strftime('%Y-%m-%d')),
        city=request.form.get('city', 'Unknown City'),
        country=request.form.get('country', 'Unknown Country'),
        description=request.form.get('description', 'No Description')
    )
    events.append(new_event)
    save_events(events)
    return redirect(url_for('calendar.calendar_page'))

def is_future_event(event):
    event_date = datetime.strptime(event.date, "%Y-%m-%d").date()
    return event_date >= datetime.now().date()ate, "%Y-%m-%d").date()
    except ValueError:
        return False
    return event_date >= datetime.now().date()