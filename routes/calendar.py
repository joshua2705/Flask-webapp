from flask import Blueprint, render_template, request, redirect, url_for
from services.calendar_service import save_events, get_events
from datetime import datetime, timedelta
from models.event import Event
import static.constants
import pytz

# Create Flask blueprint for the calendar
calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/calendar')
def calendar_page():
    """ 
    The calendar_page function returns the calendar page.

    Returns:
        Rendered HTML for the calendar page with the event list.
    """ 
    # Fetch events and only include future events
    events = [event for event in get_events() if is_future_event(event)]
    # events = list(filter(past_events, events))

    # Get today's date in Paris timezone
    today = datetime.now(pytz.timezone('Europe/Paris')).date()

    # Generate a list of the next 5 days, including today's date
    date_range = [(today + timedelta(days=x)).strftime('%d-%m-%Y') 
                 for x in range(5)]

    # Associate the above list with the weekday names
    day_range = [(today + timedelta(days=x)).strftime('%A') 
                 for x in range(5)]

    # Return the 'calendar.html' template with the filtered events, date range, day range, and countries
    return render_template('calendar.html', events=events, date_range=date_range, day_range=day_range, countries= static.constants.COUNTRIES)

# Route to handle adding new events with POST requests
@calendar_bp.route('/calendar/add', methods=['POST'])
def add_event():
    """
    This function adds an event to the calendar.

    Returns:
        Redirects the user back to the calendar page after saving the event.
    """
    # Fetch future events
    events = [event for event in get_events() if is_future_event(event)]

    # Create a new event from the form data, with defaults for missing fields
    new_event = Event(
        name=request.form.get('title', 'Untitled Event'),
        date=request.form.get('date', datetime.now().strftime('%d-%m-%Y')),
        city=request.form.get('city', 'Unknown City'),
        country=request.form.get('country', 'Unknown Country'),
        description=request.form.get('description', 'No Description')
    )

    # Add new event to the list and save it
    events.append(new_event)
    save_events(events)
    return redirect(url_for('calendar.calendar_page'))

def is_future_event(event):
    """
    Check if an event is in the future or today.

    Arguments:
        event (Event): The event object to check, containing a date attribute in the format "%d-%m-%Y".

    Returns:
        bool: True if the event date is today or in the future, False otherwise.
    """
    try:
        # Parse the event's date and compare it with today's date
        event_date = datetime.strptime(event.date, "%d-%m-%Y").date()
        return event_date >= datetime.now().date()
    except ValueError:
        return False
