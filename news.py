from Speak import speak
from urllib.request import urlopen
import json


def news():
    try:
        jsonObj = urlopen(
            "https://newsapi.org/v2/everything?q=tesla&from=2021-04-08&sortBy=publishedAt&apiKey=26c630d9757c4ef9b4c11a550821ff42")  # url-------------------------------
        data = json.load(jsonObj)
        i = 1

        speak("Here are some top headline for You ")
        print('=================== TOP HEADLINES ===================' + '\n')
        for item in data['articles']:
            print((str(i)) + '.' + item['title'] + '\n')
            print(item['description'] + '\n')
            speak(item['title'])
            i += 1

    except Exception as e:
        print(str(e))
