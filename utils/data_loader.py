from dotenv import load_dotenv
import os
import requests


load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = os.getenv('API_URL')
LANG = 'ru'

def load (name_city):
    response = requests.get (
        API_URL, params={'key': API_KEY, 'q': name_city, 'days': 1, 'aqi': 'yes', 'lang': LANG}
        )
    

    data = response.json()

    location = data['location']
    city_name = location['name']
    current = data['current']
    air_current = current['air_quality']

    pm2_5_cur = air_current['pm2_5']
    us_cur = air_current['us-epa-index']
    defra_cur = air_current['gb-defra-index']
    last_updated = current['last_updated']

    forecast_hours = data['forecast']['forecastday'][0]['hour']
    hours = [hour['time'][-5:] for hour in forecast_hours]
    co = [hour['air_quality']['co'] for hour in forecast_hours]
    no2 = [hour['air_quality']['no2'] for hour in forecast_hours]
    o3 = [hour['air_quality']['o3'] for hour in forecast_hours]
    so2 = [hour['air_quality']['so2'] for hour in forecast_hours]
    pm2_5 = [hour['air_quality']['pm2_5'] for hour in forecast_hours]
    pm10 = [hour['air_quality']['pm10'] for hour in forecast_hours]
    us_epa_index = [hour['air_quality']['us-epa-index'] for hour in forecast_hours]
    gb_defra_index = [hour['air_quality']['gb-defra-index'] for hour in forecast_hours]

    return {
        'location': location,
        'city_name': city_name,
        'last_updated': last_updated,
        'pm2_5_cur': pm2_5_cur,
        'us_cur': us_cur,
        'defra_cur': defra_cur,
        'hours': hours,
        'co': co,
        'no2': no2,
        'o3': o3,
        'so2': so2,
        'pm2_5': pm2_5,
        'pm10': pm10,
        'us_epa_index': us_epa_index,
        'gb_defra_index': gb_defra_index
    }



    # air_current = response_json['current']['air_quality']
    # forecast_hours = response_json['forecast']['forecastday'][0]['hour']
    # pm2_5_cur = air_current['pm2_5']
    # last_updated = air_current['last_updated']
    # defa_cur = air_current['gb-defra-index']
    # us_cur = air_current['us-epa-index']



    # location = response_json['location']
    # city_name = location['name']
    # hours = [hour['time'][-5:] for hour in forecast_hours]
    # co = [hour['air_quality']['co'] for hour in forecast_hours]
    # no2 = [hour['air_quality']['no2'] for hour in forecast_hours]
    # o3 = [hour['air_quality']['o3'] for hour in forecast_hours]
    # so2 = [hour['air_quality']['so2'] for hour in forecast_hours]
    # pm2_5 = [hour['air_quality']['pm2_5'] for hour in forecast_hours]
    # pm10 = [hour['air_quality']['pm10'] for hour in forecast_hours]
    # us_epa_index = [hour['air_quality']['us-epa-index'] for hour in forecast_hours]
    # gb_defra_index = [hour['air_quality']['gb-defra-index'] for hour in forecast_hours]



    # co = tyuj['co'] #угарный газ
    # no2 = tyuj['no2'] #диоксид азота
    # o3 = tyuj['o3'] #озон
    # so2 = tyuj['so2']  #диоксид серы
    # pm2_5 = tyuj['pm2_5']  #оценки качества воздуха
    # pm10 = tyuj['pm10']  #отражает наличие в воздухе твёрдых частиц диаметром 10 микрометров
    # us_epa_index = tyuj['us-epa-index']индекс качества воздуха США
    # gb_defra_index = tyuj['gb-defra-index'] #индекс качества воздуха DEFRA в Великобритании
    
    # return {'us_cur': us_cur,
    #         'defa_cur': defa_cur,
    #         'last_updated': last_updated,
    #         'pm2_5_cur': pm2_5_cur, 
    #         'location': location,
    #         'city_name': city_name,
    #         'hours' : hours,
    #         'co': co,
    #         'no2': no2,
    #         'o3': o3,
    #         'so2': so2,
    #         'pm2_5': pm2_5,
    #         'pm10': pm10,
    #         'us_epa_index': us_epa_index,
    #         'gb_defra_index': gb_defra_index,
    #         'air_current': air_current
    #         }
