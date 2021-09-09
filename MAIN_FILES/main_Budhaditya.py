import sys
from CORE.Speak import speak
from BASIC_FUNCTIONALITIES.calculate import calculate
from CORE.lrs import logout, restart, shutdown
import wolframalpha
# from sleep import sleep
from BASIC_FUNCTIONALITIES.whatsappMessage import WhatsAppMessage
from BASIC_FUNCTIONALITIES.ReadSelectedText import read
from BASIC_FUNCTIONALITIES.WeatherUpdates import weather
from BASIC_FUNCTIONALITIES.Alarm import alarm
from OPEN_APPS.Camera import Cam
from BASIC_FUNCTIONALITIES.batterycheck import BatteryInfo
from BASIC_FUNCTIONALITIES.remember import remember_that,remember_anything
from CORE.CloseJarvis import ExitYourself
from BASIC_FUNCTIONALITIES.WeatherByPritam import WeatherTemp
import pyttsx3
#from SEARCH_FUNCTIONS import Chrome
#from SEARCH_FUNCTIONS.SearchOnline import GoogleSearch, BingSearch
from SEARCH_FUNCTIONS.YouTube import YouTubeSearch
from CORE.TakeCommand import TakeCommand
#from SEARCH_FUNCTIONS.Wikipedia import wiki
from BASIC_FUNCTIONALITIES.WishMe import WishMe
from BASIC_FUNCTIONALITIES.SendEmail import tryout, exception
from BASIC_FUNCTIONALITIES.DateAndTime import date, time
from BASIC_FUNCTIONALITIES.cpu import cpu
from PLAY_GAMES.joke import joke
from PLAY_GAMES.flipacoin import flip
from PLAY_GAMES.rolladice import roll
from PLAY_GAMES.rck_ppr_scr import RockPaperScissor
from BASIC_FUNCTIONALITIES.screenshot import screenshot
from SEARCH_FUNCTIONS.news import news
from SEARCH_FUNCTIONS.music import music
from SEARCH_FUNCTIONS.WikiHow import HowTo
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

        elif 'wikipedia' in query:
            HowTo(query)

        elif 'send email' in query:
            try:
                tryout()
            except:
                exception()

        #elif 'search internet' in query:
         #   Chrome.ChromeSearch()

        elif 'search youtube' in query:
            YouTubeSearch()

        #elif 'search google' in query:
         #   GoogleSearch()
            
        elif 'battery' in query:
            BatteryInfo()

        elif 'weather' or 'temperature' or 'humidity' in query:
            WeatherTemp(query)

        elif 'stop' in query:
            ExitYourself()

        #elif 'search bing' in query:
         #   BingSearch()

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
            locate(query)

        elif 'open app' in query:
            app()

        elif 'open my documents' in query:
            os.system('explorer C://{}'.format(query.replace('Open','')))

        elif 'generate password' in query:
            passwordgen()

        elif 'calculate' in query:
            calculate(query)

        elif 'what is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")

        # elif 'stop Listening' in query: # Not Working
        #     sleep()

        elif 'logout' in query:  # Logout, restart and shutdown not working
            logout()
        elif 'restart' in query:
            restart()
        elif 'shutdown' in query:
            shutdown()

        elif 'whatsapp message' in query:
            WhatsAppMessage()

        elif 'Weather' in query:
            weather()

        elif 'read' in query:
            read()

        elif 'alarm' in query:
            # speak("At what time should I set the alarm? For example set the alarm to 6:00 am")
            tt = query.replace("set the alarm to ", "")
            tt = tt.replace(".", "")
            tt = tt.upper()
            alarm(tt)

        elif 'camera' in query:
            Cam()

        elif 'go offline' in query:
            offline()

        elif 'remember that' in query:

            tc = query.replace("remember that ", "")
            remember_that(tc)

        elif 'remember anything' in query:
            remember_anything()

        elif 'screenshot' in query:
            screenshot()

        elif 'toss' in query:
            flip()

        elif 'roll a dice' in query:
            roll()

        elif 'rock paper scissor' in query:
            RockPaperScissor()




        