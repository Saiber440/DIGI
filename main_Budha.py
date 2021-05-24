import pyttsx3
import Chrome
from SearchGoogle import GoogleSearch
from YouTube import YouTubeSearch
from TakeCommand import TakeCommand
from Wikipedia import wiki
from WishMe import WishMe
from SendEmail import tryout, exception
from DateAndTime import date, time
from cpu import cpu
from joke import joke
from Speak import speak
from screenshot import screenshot
from calculate import calculate
from lrs import logout, restart, shutdown
import wolframalpha
from sleep import sleep
from news import news
from music import music
from remember import remember_that, remember_anything
from note import write_note,show_note
from location import locate
from offline import offline
from word import word
from whatsappMessage import WhatsAppMessage
from ReadSelectedText import read
from WeatherUpdates import weather


from App import app
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
            wiki()

        elif 'send email' in query:
            try:
                tryout()
            except:
                exception()

        elif 'search internet' in query:
            Chrome.ChromeSearch()

        elif 'search youtube' in query:
            YouTubeSearch()

        elif 'search google' in query:
            GoogleSearch()


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

        elif 'stop Listening' in query: # Not Working
            sleep()

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
