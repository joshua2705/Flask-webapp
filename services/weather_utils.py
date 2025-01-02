from datetime import datetime

# Temperature unit conversion
def tempConvert(kelvin, unit):
    """
    Converts temperature from Kelvin to Celsius or Fahrenheit.

    Arguments:
        kelvin (float): Temperature in Kelvin.
        unit (str): Target temperature unit ('C' for Celsius or 'F' for Fahrenheit).
    Returns:
        float: Temperature in the specified unit, rounded to one decimal place.
    """
    return (kelvin - 273.15) if unit == 'C' else (kelvin - 273.15) * 1.8 + 32

# Function to generalize weather conditions
def simplify_condition(main):
    """
    Simplify the 'main' weather condition to a more generalized form.

    Arguments:
        main (str): the main weather condition for the API
    Returns:
        Simplified weather condition
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

    Arguments:
        current_data (dict): Weather data for the current moment.
        unit (str): Target temperature unit ('C' or 'F').
    Returns:
        dict: Formatted weather data including temperature, condition, and humidity.
    """
    return {
        'temp': round(tempConvert(current_data['main']['temp'], unit)),
        'condition': simplify_condition(current_data['weather'][0]['main']), 
        'humidity': current_data['main']['humidity'] 
    }

def select_image(condition):
    """
    Selects an image based on the weather condition

    Arguments: 
        condition (str): Weather condition
    Returns:
        str: Image URL (Filename of the corresponding image)
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

    Arguments:
        forecast_data (dict): Raw forecast data from the weather API.
        unit (str): Target temperature unit ('C' or 'F').
    Returns:
        list: A list of dictionaries containing day, temperature, and weather condition.   
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
    """
    Find the forecast weather data for a specific day.

    Arguments:
        forecast_data (dict): Raw forecast data from the weather API.
        forecast_date (str): Date for which to find the weather forecast in 'dd-mm-yyyy' format.
    Returns:
        dict: Weather data for the specified date or a default response if not found.
    """
    forecast_date = datetime.strptime(forecast_date,'%d-%m-%Y')
    
    for i in range(0, len(forecast_data['list']), 8):  # Each data point is 3 hours apart
        day_data = forecast_data['list'][i]
        day_forecast = datetime.strptime(day_data['dt_txt'].split()[0],'%Y-%m-%d')
        
        if forecast_date == day_forecast:
            return day_data
    
    return [{
        'weather': [{"main":"Null"}]
    }]
