# modules and global variables
from abc import ABC, abstractmethod #abc means abstract base classes
import requests

# abstract class
class WeatherAbstract(ABC):

    @abstractmethod
    def get_current_weather(self,lat,lon):
        pass


# openweather class
class OpenWeatherProvider(WeatherAbstract):
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    def __init__(self,api_key):
        self.api_key = api_key

    def get_current_weather(self, lat, lon):
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
        }
        response = requests.get(self.base_url, params)
        normalized_data = {"temp": float(response.json()["main"]["temp"]) - 273.15 ,
                           "humidity": response.json()["main"]["humidity"]}
        return normalized_data



#open meteo class
class OpenMeteoProvider(WeatherAbstract):
    base_url = "https://api.open-meteo.com/v1/forecast"
    def get_current_weather(self,lat,lon):
        params = {
            "exclude" : "hourly",
            "latitude" : lat,
            "longitude" : lon,
            "current" : "temperature_2m,relative_humidity_2m"
        }
        response = requests.get(self.base_url,params)
        normalized_data = {"temp": response.json()["current"]["temperature_2m"] ,
                           "humidity": response.json()["current"]["relative_humidity_2m"]}
        return normalized_data




#running the application
meteo_provider = OpenMeteoProvider()
open_weather_provider = OpenWeatherProvider("91ef236cc9290c783d3e6572ecc7fd35")
print(open_weather_provider.get_current_weather(35.69313513805353,51.39946207974878))
print(meteo_provider.get_current_weather(35.69313513805353,51.39946207974878))