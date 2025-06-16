from dotenv import load_dotenv
import os
import requests


load_dotenv()
API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')
LANG = 'ru'

def load_data(name_city):
    response = requests.get(
        API_URL, 
        params={
            'key': API_KEY, 
            'q': name_city, 
            'days': 1, 
            'aqi': 'no', 
            'lang': LANG
        }
    )
    data = response.json()

    location = data['location']
    forecast_hours = data['forecast']['forecastday'][0]['hour']
    current = data['current']
    
    return {
        "city_name": location['name'],
        "icon": current['condition']['icon'],
        "temp": current['temp_c'],
        "condition": current['condition']['text'],
        "hours": [h['time'][-5:] for h in forecast_hours],
        "temps": [h['temp_c'] for h in forecast_hours],
        "ap": [h['pressure_mb'] * 0.75 for h in forecast_hours],
        "humidity": [h['humidity'] for h in forecast_hours],
        "wind": [h['wind_kph'] * 0.28 for h in forecast_hours],
        "wind_dirs": [h['wind_degree'] for h in forecast_hours],
    }