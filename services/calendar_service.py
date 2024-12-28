import json
from pathlib import Path
from models.event import Event

def save_events(events_data):
    with open('events.json', 'w') as f:
        json.dump([event.to_dict() for event in events_data], f)

def get_events():
    if Path('events.json').exists():
        with open('events.json', 'r') as f:
            return [Event.from_dict(event) for event in json.load(f)]
    return []
