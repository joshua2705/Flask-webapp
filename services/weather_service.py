def get_weather_forecast():
    # Simulated weather data (in a real app, you'd call a weather API)
    return {
        'current': {
            'temp': 22,
            'condition': 'Sunny',
            'humidity': 65
        },
        'forecast': [
            {'day': 'Monday', 'temp': 23, 'condition': 'Sunny'},
            {'day': 'Tuesday', 'temp': 20, 'condition': 'Cloudy'},
            {'day': 'Wednesday', 'temp': 19, 'condition': 'Rain'}
        ]
    }