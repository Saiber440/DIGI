import requests
from bs4 import BeautifulSoup
from Speak import speak


def WeatherTemp(query):
    search = query
    url = f"https://google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"Current Temperature {search} is {temp}")
