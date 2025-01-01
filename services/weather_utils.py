from datetime import datetime

# Temperature unit conversion
def tempConvert(kelvin, unit):
    """
    Convert temperature from Kelvin to Celsius or Fahrenheit.
    """
    return (kelvin - 273.15) if unit == 'C' else (kelvin - 273.15) * 1.8 + 32

# Function to generalize weather conditions
def simplify_condition(main):
    """
    Simplify the 'main' weather condition to a more generalized form.
    """
    main = main.lower()
    if main in ["smoke", "haze", "dust", "fog", "sand", "ash", "squall"]:
        return "Mist"
    elif main in ["drizzle"]:
        return "Rain"
    return main.capitalize()  # Default condition

def format_current_weather(current_data, unit):
    """
    Format the current weather data into a dictionary for rendering.
    """
    return {
        'temp': round(tempConvert(current_data['main']['temp'], unit)),
        'condition': simplify_condition(current_data['weather'][0]['main']), 
        'humidity': current_data['main']['humidity'] 
    }

def select_image(condition):
    """
    Selects an image based on the weather condition
    Args: condition (str): Weather condition
    Returns:str: Image URL (Filename of the corresponding image)
    """
    images = {
        "Sunny": "images/clearsky.png",
        "Clouds": "images/cloudy.png",
        "Rain": "images/rain.png",
        "Mist": "images/mist.png",
        "Snow": "images/snow.png",
        "Thunderstorm": "images/thunderstorm.png",
        "Drizzle": "images/drizzle.png",
        "Tornado": "images/tornado.png",
    }
   # Return the image if the condition matches, otherwise return a default image.
    return images.get(condition, "images/default.png")

# Function to format forecast weather data
def format_forecast_weather(forecast_data, unit):
    """
    Format the forecast data into a list of simplified weather dictionaries.
    """
    forecast = []
    # Simplified forecast: picking every 8th data point for 3 days (roughly one per day)
    for i in range(8, len(forecast_data['list']) - 8, 8):  # Each data point is 3 hours apart
        day_data = forecast_data['list'][i]
        forecast.append({
            'day': datetime.strptime(day_data['dt_txt'].split()[0],'%Y-%m-%d').strftime("%A"),  # Extract date
            'temp': round(tempConvert(day_data['main']['temp'], unit)),
            'condition': simplify_condition(day_data['weather'][0]['main'])
        })
    return forecast

# Function to find the forecast weather data for a particular day
def find_forecast_weather(forecast_data, forecast_date):

    forecast_date = datetime.strptime(forecast_date,'%d-%m-%Y')
    
    for i in range(0, len(forecast_data['list']), 8):  # Each data point is 3 hours apart
        day_data = forecast_data['list'][i]
        day_forecast = datetime.strptime(day_data['dt_txt'].split()[0],'%Y-%m-%d')
        
        if forecast_date == day_forecast:
            return day_data
    
    return [{
        'weather': [{"main":"Null"}]
    }]
