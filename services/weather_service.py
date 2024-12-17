import sys
import urllib.parse
import requests
import pycountry

WEATHER_API_URI = "https://api.openweathermap.org/data/2.5/weather"
GEO_API_URI = "http://api.openweathermap.org/geo/1.0/direct"
API_KEY = "0e2ca89ed39d35cefc9a599038e33413"  # Replace with your actual API key

def get_country_name(country_code):
    """Convert a country code (e.g., 'GB') to its full name (e.g., 'United Kingdom')."""
    try:
        return pycountry.countries.get(alpha_2=country_code).name
    except AttributeError:
        return country_code
    
def search_city(query):
    '''
    Look for a given city. If multiple options are returned, have the user choose between them.
    Return one city (or None)
    '''
    url = GEO_API_URI
    #cities = requests.get(url, params={'q': query, 'appid': API_KEY}).json()
    cities = requests.get(url, params={'q': query, 'limit': 5, 'appid': API_KEY}).json()

    if not cities:
        print(f"Sorry, OpenWeather does not know about {query}!")
        return None

    unique_cities = {}
    for city in cities:
        key = (city['name'], city['country']) 
        if key not in unique_cities:
            unique_cities[key] = city

    cities = list(unique_cities.values())
    if len(cities) == 1:
        return cities[0]

    for i, city in enumerate(cities):
        country_full_name = get_country_name(city['country'])
        print(f"{i + 1}. {city['name']}, {country_full_name}")
        #print(f"{i + 1}. {city['name']}, {city['country']}")

    index = int(input("Multiple matches found, which city did you mean?\n> ")) - 1
    return cities[index]

def get_weather(city):
    '''
    Fetch the weather for a given city using OpenWeatherMap API.
    '''
    city_name = city['name']
    country_code = city['country']
    url = f"{WEATHER_API_URI}?q={city_name},{country_code}&appid={API_KEY}"
    response = requests.get(url)
    weather_data = response.json()
    

    if response.status_code != 200:
        print(f"Failed to get weather data: {weather_data.get('message', 'Unknown error')}")
        return None
    
    if unit == 'C':
        current_temp = weather_data['main']['temp'] - 273.15
        feels_like_temp = weather_data['main']['feels_like'] - 273.15
        unit_label = "°C"
    else:
        current_temp = (weather_data['main']['temp'] - 273.15) * 1.8 + 32
        feels_like_temp = (weather_data['main']['feels_like'] - 273.15) * 1.8 + 32
        unit_label = "F"
        
    print(f"Weather in {city['name']}: {weather_data['weather'][0]['description']}")
    print(f"Current temperature: {current_temp:.2f}{unit_label}")
    print(f"The current temperature feels like: {feels_like_temp:.2f}{unit_label}")
if __name__ == "__main__":
    query = input("Enter a city name: ")
    city = search_city(query)
    if city:
        unit = input("Do you want the temperature in Fahrenheit or Celsius? (F/C): ").strip().upper()
        weather = get_weather(city)
        if weather:
            temp_kelvin = weather['main']['temp']
            if unit == 'C':
                temp_celsius = temp_kelvin - 273.15
                print(f"Weather in {city['name']}, {city['country']}: {weather['weather'][0]['description']}, Temperature: {temp_celsius:.2f}°C")
            else:
                print(f"Weather in {city['name']}, {city['country']}: {weather['weather'][0]['description']}, Temperature: {temp_kelvin}°F")