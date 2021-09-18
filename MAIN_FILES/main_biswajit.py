import pyttsx3

from BASIC_FUNCTIONALITIES.CheckInternetSpeed import InternetSpeed
# from SEARCH_FUNCTIONS import Chrome
# from SEARCH_FUNCTIONS.SearchOnline import GoogleSearch
from SEARCH_FUNCTIONS.WikiHow import HowTo
from SEARCH_FUNCTIONS.YouTube import YouTubeSearch
from CORE.TakeCommand import TakeCommand
from SEARCH_FUNCTIONS.SearchOnline import SearchOnline
from BASIC_FUNCTIONALITIES.WishMe import WishMe
from BASIC_FUNCTIONALITIES.SendEmail import tryout, exception
from BASIC_FUNCTIONALITIES.DateAndTime import date, time
from BASIC_FUNCTIONALITIES.cpu import cpu
from PLAY_GAMES.joke import joke
from PLAY_GAMES.flipacoin import flip
from PLAY_GAMES.rolladice import roll
from BASIC_FUNCTIONALITIES.screenshot import screenshot
from SEARCH_FUNCTIONS.news import news
# from SEARCH_FUNCTIONS.music import music
# from BASIC_FUNCTIONALITIES.remember import remember_that, remember_anything
from BASIC_FUNCTIONALITIES.note import write_note,show_note
from SEARCH_FUNCTIONS.location import locate
from CORE.offline import offline
# from word import word
from OPEN_APPS.App import app
import os
from Pswgen import passwordgen
# ====================================================
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wolframalpha_app_id = 'EJ3QJT-2YHHU3AYK7'
# ========================================


# ========================== Pritam Day =========================


if __name__ == '__main__':

    WishMe()

    while True:

        query = TakeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'search' in query:
            SearchOnline()

        # elif 'how to' in query:
        #     HowTo(query)



        elif 'send email' in query:
            try:
                tryout()
            except:
                exception()

        # elif 'search internet' in query:
        #     Chrome.ChromeSearch()

        elif 'play' or 'youtube' in query:
            YouTubeSearch()

        # elif 'search google' in query:
        #     GoogleSearch()

        # ========================== Biswajit Kar =========================

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'go offline' in query:
            offline()

        # elif 'msword' in query:
        #     word()

        elif 'write a note ' in query:
            write_note()

        elif 'Show me notes' in query:
            show_note()

        elif 'screenshot' in query:
            screenshot()

        elif 'play music' in query:
            music()

        # elif 'remember that' in query:
        #     remember_that()
        #
        # elif 'do you remember anything' in query:
        #     remember_anything()

        elif 'news' in query:
            news()

        elif 'where is' in query:
            locate()

        elif 'open app' in query:
            app()

        elif 'open my document' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))

        elif 'generate password' in query:
            passwordgen()

        elif 'toss' in query:
            flip()

        elif 'roll a dice' in query:
            roll()
