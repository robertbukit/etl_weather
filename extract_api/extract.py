import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_url = "https://api.weatherstack.com/current"

params = {
    "access_key": os.getenv("ACCESS_KEY"),
    "query": "New York"
}

def fetch_data():
    try:
        response = requests.get(api_url, params)

        if response.status_code == 200:
            data = response.json()
            return data
        
        else:
            print(f"Gagal koneksi ke server. HTTP status: {response.status_code}")

    except Exception as e:
        print(e)
        raise

    # versi simple untuk ekstraksinya bisa seperti berikut ini saja
    # response = requests.get("https://api.weatherstack.com/current? access_key=YOUR_ACCESS_KEY& query = New York")

# fetch_data()

def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-10-29 12:13', 'localtime_epoch':1793275980, 'utc_offset': '-4.0'}, 'current': {'observation_time': '04:13 PM', 'temperature': 18, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '07:23 AM', 'sunset': '05:56 PM', 'moonrise': '08:31 PM', 'moonset': '11:43 AM', 'moon_phase': 'Waning Gibbous', 'moon_illumination': 89}, 'air_quality': {'co': '191', 'no2': '26.3', 'o3': '60', 'so2': '3.4', 'pm2_5': '16.2', 'pm10': '20.3', 'us-epa-index': '2', 'gb-defra-index': '2'},'wind_speed': 13, 'wind_degree': 219, 'wind_dir': 'SW', 'pressure': 1024, 'precip': 0, 'humidity': 55, 'cloudcover': 0, 'feelslike': 15, 'uv_index': 3, 'visibility': 10, 'is_day': 'yes'}}