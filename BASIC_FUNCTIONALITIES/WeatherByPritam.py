import requests
from bs4 import BeautifulSoup
from CORE.Speak import speak


def WeatherTemp():
    search = "Temperature in Delhi"
    url = f"https://google.com/search?q=(search)"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"Current (search) is (temp)")
