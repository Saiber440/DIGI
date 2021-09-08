from CORE.Speak import speak
from urllib.request import urlopen
import json


def news():
    try:
        jsonObj = urlopen(
            "https://newsapi.org/v2/everything?q=tesla&from=2021-08-08&sortBy=publishedAt&apiKey=eea1fa3cfd014438a9190b5cf0fb4949")  # url-------------------------------
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


#import requests
#
# url = "https://bing-news-search1.p.rapidapi.com/news/trendingtopics"
#
# querystring = {"safeSearch":"Off","textFormat":"Raw"}
#
# headers = {
#     'x-bingapis-sdk': "true",
#     'x-rapidapi-host': "bing-news-search1.p.rapidapi.com",
#     'x-rapidapi-key': "90bc66677cmsh388c8ecd3ec6cbdp117ebcjsne01bd9f163dd"
#     }
#
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)