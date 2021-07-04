import pyttsx3
from SEARCH_FUNCTIONS import Chrome
from SEARCH_FUNCTIONS.SearchOnline import GoogleSearch
from SEARCH_FUNCTIONS.YouTube import YouTubeSearch
from CORE.TakeCommand import TakeCommand
from SEARCH_FUNCTIONS.Wikipedia import wiki
from BASIC_FUNCTIONALITIES.WishMe import WishMe
from BASIC_FUNCTIONALITIES.SendEmail import tryout, exception
from BASIC_FUNCTIONALITIES.DateAndTime import date, time
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
from BASIC_FUNCTIONALITIES.screenshot import screenshot
from BASIC_FUNCTIONALITIES.note import write_note,show_note
from BASIC_FUNCTIONALITIES.cpu import cpu
from CORE.offline import offline
from BASIC_FUNCTIONALITIES.remember import remember_that,remember_anything
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
            wiki()

        elif 'send email' in query:
            try:
                tryout()
            except:
                exception()

        elif 'search internet' in query:
            Chrome.ChromeSearch()

        elif 'battery' in query:
            BatteryInfo()

        elif 'cpu' in query:
            cpu()

        elif 'search youtube' in query:
            YouTubeSearch()

        elif 'search google' in query:
            GoogleSearch()

        elif 'screenshot' in query:
            screenshot()

        elif 'write a note' in query:
            write_note()

        elif 'show me notes' in query:
            show_note()


        # ============================= Budhaditya Sarkar ===================================

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

        elif 'logout' in query: # Logout, restart and shutdown not working
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
            #speak("At what time should I set the alarm? For example set the alarm to 6:00 am")
            tt = TakeCommand()
            tt = tt.replace("set the alarm ", "")
            tt = tt.replace(".","")
            tt = tt.upper()
            alarm(tt)

        elif 'camera' in query:
            Cam()

        elif 'go offline' in query:
            offline()

        elif 'remember that' in query:
            tc = TakeCommand()
            tc = tc.replace("remember that ", "")
            remember_that(tc)

        elif 'remember anything' in query:
            remember_anything(remember_that(tc))


