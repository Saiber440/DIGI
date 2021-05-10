import pyttsx3
import wikipedia
from TakeCommand import TakeCommand
from WishMe import WishMe
from SendEmail import SendEmail
from DateAndTime import datetime, time, date
from cpu import cpu
from joke import joke
from Speak import speak
from screenshot import screenshot
import os
import random
import json
from urllib.request import urlopen
import webbrowser as wb
import wolframalpha
import time
import pywhatkit
# ====================================================
engine = pyttsx3.init()
voices=engine.getProperty('voices')
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
            speak("Searching...")
            query = query.replace("Wikipedia", "")
            result = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = TakeCommand()
                speak("Who is the receiver?")
                receiver = input("Enter Receiver Email :")
                to = receiver
                SendEmail(to, content)
                speak(content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Unable to send")



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
            ma_word = r' ==============================.exe'           # path for the app
            os.startfile(ma_word)


        elif'write a note ' in query:
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
            speak('What should I play for you?')
            ans = TakeCommand().lower()
            speak('playing ' + ans)
            pywhatkit.playonyt(ans)


        elif 'remember that' in query:
            speak("What should I remember Sir?")
            memory = TakeCommand()
            speak("You asked me to remember that"+memory)
            remember = open(('memory.txt', 'w'))
            remember.write(memory)
            remember.close()
        elif 'do you remember anything' in query:
            remember = open('memory.txt', 'r')
            speak(' You asked me to remember that '+remember.read())



        elif 'news' in query:
            try:
                jsonObj = urlopen("https://newsapi.org/v2/everything?q=tesla&from=2021-04-08&sortBy=publishedAt&apiKey=26c630d9757c4ef9b4c11a550821ff42")    # url-------------------------------
                data = json.load(jsonObj)
                i = 1


                speak("Here are some top headline for You ")
                print('=================== TOP HEADLINES ==================='+'\n')
                for item in data['articles']:
                    print((str(i))+'.'+item['title'] + '\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i += 1

            except Exception as e:
                print(str(e))



        elif'where is' in query:
            query = query.replace("where is", " ")
            location = query
            speak("User asked to locate "+location)
            wb.open_new_tab("https://www.google.com/maps/place"+location)


# ============================= Budhaditya Sarkar ===================================
        elif 'calculate' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(''.join(query))
            answer = next(res.results).text
            print("The answer is : " + answer)
            speak("The answer is " + answer)

        elif 'what is' in query or 'who is' in query:
            client = wolframalpha.Client(wolframalpha_app_id)
            res = client.query(query)
            try:
                print(next(res.results).text)
                speak(next(res.results).text)
            except StopIteration:
                print("No Results")

        elif 'stop Listening' in query:
            speak('For how many seconds should I stop listening?')
            ans=int(TakeCommand())
            time.sleep(ans)
            print(ans)
