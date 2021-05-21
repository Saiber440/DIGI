from TakeCommand import TakeCommand
from Speak import speak
import requests


def weather():
    speak('For which city you want to know about the weather?')
    city = TakeCommand()

    url = ('http://api.openweathermap.org/data/2.5/weather?='+city+ '&units=imperial&appid=04478687ea37ce0e60bebbc803a5ac33')
    res = requests.get(url)
    data = res.json()
    weather = data['weather'] [0] ['main']
    temp = data['main']['temp']
    desp = data['weather'] [0] ['description']
    print(weather)
    print(temp)
    print(desp)