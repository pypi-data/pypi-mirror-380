import requests
import os
from dotenv import load_dotenv
import pprint

load_dotenv()
api_key = os.environ.get("API_KEY_WEATHER")

class WeatherBuddy:
    """
    Fetches and processes weather data from OpenWeatherMap API.
    Usage:
        weather = WeatherBuddy(api_key, city="London")
        print(weather.next_12_hours_simplified())
    Output: List of (time, temperature, description) for next 12 hours (Celsius).
    """
    def __init__(self, api_key, city=None, lat=None, lon=None):
        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&APPID={api_key}&units=metric"
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&APPID={api_key}&units=metric"
        else:
            raise ValueError("Either city or both lat and lon must be provided.")
        response = requests.get(url)
        self.data = response.json()
        if self.data.get("cod") != "200":
            raise Exception(f"API error: {self.data.get('message')}")

    def next_12_hours(self):
        return self.data['list'][:4]

    def next_12_hours_simplified(self):
        hours = self.next_12_hours()
        return [(item["dt_txt"], round(item["main"]["temp"]), item["weather"][0]["description"]) for item in hours]

city = input("What city do you want the weather for? ")
weather = WeatherBuddy(api_key, city)
print(f"Weather forecast for {city} for the next 12 hours:")
pprint.pprint(weather.next_12_hours_simplified())

