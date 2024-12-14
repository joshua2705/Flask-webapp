from flask import Blueprint, render_template, request, redirect, url_for
from services.calendar_service import add_event, get_events

calendar_bp = Blueprint('calendar', __name__)

@calendar_bp.route('/calendar')
def calendar_page():
    events = get_events()
    return render_template('calendar.html', events=events)

@calendar_bp.route('/calendar/add', methods=['POST'])
def add_calendar_event():
    event_data = {
        'title': request.form.get('title'),
        'date': request.form.get('date'),
        'description': request.form.get('description')
    }
    add_event(event_data)
    return redirect(url_for('calendar.calendar_page'))