import pyttsx3
from TakeCommand import TakeCommand
from Wikipedia import wiki
from WishMe import WishMe
from SendEmail import tryout, exception
from DateAndTime import datetime, date, time
from cpu import cpu
from joke import joke
from Speak import speak
from screenshot import screenshot
import os
import random
import json
from urllib.request import urlopen
import webbrowser as wb
from calculate import calculate
from sleep import sleep
from lrs import logout
from lrs import restart
from lrs import shutdown
import pywhatkit



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

            speak("What should I Write, Sir? ")
            notes = TakeCommand()
            file = open('notes.txt', 'w')
            speak("Sir Should I include date and time ")
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans or 'yup' in ans or 'yaa' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('I got your note ,Sir!')
            else:
                file.write(notes)


        elif 'Show me notes' in query:

            speak('Showing NOTES')
            file = open('notes.txt', 'r')
            print(file.read())
            speak(file.read())


        elif 'screenshot' in query:

            screenshot()


        elif 'play music' in query:

            speak('You like to listen Online or Offline?')
            ans = TakeCommand().lower()
            if 'online' in ans:
                ans = TakeCommand().lower()
                speak('What should I play for you?')
                ans = TakeCommand().lower()
                speak('playing ' + ans)
                pywhatkit.playonyt(ans)


            elif 'offline' in query:

                songs_dir = 'C:\music'  # path-----------------------------
                music = os.listdir(songs_dir)
                speak('What should I play for you?')
                speak('Select a number....')
                ans = TakeCommand().lower()
                while 'number' not in ans and ans != 'random' and ans != 'you choose':
                    speak('I could not understand you . Please try again.')
                    ans = TakeCommand().lower()
                if 'number' in ans:
                    no = int(ans.replace('number', ''))
                elif 'random' or 'you choose' in ans:
                    no = random.randint(1, 100)
                    os.startfile(os.path.join(songs_dir, music[no]))


        elif 'remember that' in query:

            speak("What should I remember Sir?")
            memory = TakeCommand()
            speak("You asked me to remember that" + memory)
            remember = open(('memory.txt', 'w'))
            remember.write(memory)
            remember.close()


        elif 'do you remember anything' in query:

            remember = open('memory.txt', 'r')
            speak(' You asked me to remember that ' + remember.read())


        elif 'news' in query:

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
