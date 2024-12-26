

# Temperature unit conversion
def tempConvert(kelvin, unit):
    return (kelvin - 273.15) if unit == 'C' else (kelvin - 273.15) * 1.8 + 32

# Function to generalize weather conditions
def simplify_weather(description):
    description = description.lower()
    if description in ["few clouds", "scattered clouds", "broken clouds", "overcast clouds"]:
        return "Cloudy"
    elif description in ["shower rain", "rain", "light rain", "moderate rain"]:
        return "Rainy"
    elif description in ["mist", "haze"]:
        return "Misty"
    return description.capitalize()  # Default condition

def format_current_weather(current_data, unit):
    return {
        'temp': round(tempConvert(current_data['main']['temp'], unit)),
        'condition': simplify_weather(current_data['weather'][0]['description']),
        'humidity': current_data['main']['humidity']
    }

def format_forecast_weather(forecast_data, unit):
    forecast = []
    # Simplified forecast: picking every 8th data point 3 days (roughly one per day)
    for i in range(8, len(forecast_data['list'])-8, 8):  # Each data point is 3 hours apart
        day_data = forecast_data['list'][i]
        forecast.append({
            'day': day_data['dt_txt'].split()[0],  # Extract date
            'temp': round(tempConvert(day_data['main']['temp'], unit)),
            'condition': simplify_weather(day_data['weather'][0]['description'])
        })
    return forecast
    