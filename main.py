import pyttsx3
from TakeCommand import TakeCommand
from Wikipedia import wiki
from WishMe import WishMe
from SendEmail import tryout, exception
from DateAndTime import date, time
from cpu import cpu
from joke import joke
from Speak import speak
from screenshot import screenshot
import os
from music import music
from note import write_note
from note import show_note
from remember import remember_that
from remember import remember_anything
from news import news
import webbrowser as wb
from calculate import calculate
from sleep import sleep
from lrs import logout
from lrs import restart
from lrs import shutdown

# ====================================================
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

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


        elif 'who is' in query:

            wiki(query)


        elif 'send email' in query:

            try:
                tryout()
            except:
                exception()


# ========================== Biswajit Kar =========================


        elif 'cpu' in query:

            cpu()


        elif 'joke' in query:

            joke()


        elif 'go offline' in query:

            speak('Going offline Sir!  See yaa')
            quit()


        elif 'word' in query:

            speak('Opening MS word...')
            ma_word = r' ==============================.exe'  # path for the app
            os.startfile(ma_word)


        elif 'write a note ' in query:
            write_note()


        elif 'Show me notes' in query:

            show_note()


        elif 'screenshot' in query:

            screenshot()


        elif 'play music' in query:
            music(query)

        elif 'remember that' in query:

            remember_that()

        elif 'do you remember anything' in query:
            remember_anything()

        elif 'news' in query:
            news()

        elif 'where is' in query:

            query = query.replace("where is", " ")
            location = query
            speak("User asked to locate " + location)
            wb.open_new_tab("https://www.google.com/maps/place" + location)


 # ============================= Budhaditya Sarkar ===================================


        elif 'calculate' in query:

            calculate(query)

        elif 'stop Listening' in query:  # not speaking and not working
            sleep()

        elif 'log out' in query:  # Not working
            logout()  # imported from lrs
        elif 'restart' in query:
            restart()
        elif 'shutdown' in query:
            shutdown()
