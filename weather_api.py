from typing import Final
import requests
from model import Weather,dt
import json

API_KEY: Final[str]= '7e26a633891c1d980270d8fbb29ce728'
BASE_URL: Final[str]= 'https://api.openweathermap.org/data/2.5/forecast'

def get_weather(city_name: str, mock:bool = True) -> dict:
    if mock:
        with open('dummy_data.json') as file:
            return json.load(file)

    #request live data
    playload: dict= {'q': city_name, 'appid':API_KEY, 'units':'metric' }
    request= requests.get(url=BASE_URL,params= playload)
    data: dict= request.json()

    return data

def get_weather_detals(weather: dict) -> list[Weather]:
    days: list[dict]=weather.get('list')

    if not days:
        raise Exception(f'Problem with json:{weather}')
    list_of_weather: list[Weather]=[]
    for day in days:
        w: Weather = Weather(date=dt.fromtimestamp(day.get('dt')),
                             details=(details := day.get('main')),
                             temp=details.get('temp'),
                             weather=(weather:= day.get('weather')),
                             description=weather[0].get('description'))
        list_of_weather.append(w)
    return list_of_weather

if __name__ =='__main__':
    current_weather: dict= get_weather('tokyo',mock=False)
    weather: list[Weather]= get_weather_detals(current_weather)

    for w in weather:
        print(w)