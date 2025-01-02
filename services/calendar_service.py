import json
from pathlib import Path
from models.event import Event

def save_events(events_data):
    """
    Saves the list of Event objects to a JSON file (events.json).
  
    Arguments:
        events_data (list): A list of Event objects to be saved.
    """
    with open('events.json', 'w') as f:
        #Convert each Event object to a dictionary and save as JSON
        json.dump([event.to_dict() for event in events_data], f)

def get_events():
    """
    Retrieves a list of Event objects from the JSON file (events.json).
    
    Returns:
        list: A list of Event objects retrieved from the JSON file.      
        If the file doesn't exist, an empty list is returned.
    """
    if Path('events.json').exists():
        with open('events.json', 'r') as f:
            return [Event.from_dict(event) for event in json.load(f)]
    return []
