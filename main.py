import pyttsx3
import wikipedia

from TakeCommand import TakeCommand
from WishMe import WishMe
from SendEmail import SendEmail

engine = pyttsx3.init()
import datetime


if __name__ == '__main__':

    WishMe()

    while True:
        query = TakeCommand().lower()

        if 'time' in query:
            datetime.time()
        elif 'date' in query:
            datetime.date()
        elif 'wikipedia' in query:
            pyttsx3.speak("Searching...")
            query = query.replace("Wikipedia", "")
            result = wikipedia.summary(query, sentences = 3)
            pyttsx3.speak("According to Wikipedia")
            print(result)
            pyttsx3.speak(result)
        elif 'send email' in query:
            try:
                pyttsx3.speak("What should I say?")
                content = TakeCommand()
                pyttsx3.speak("Who is the receiver?")
                receiver = input("Enter Receiver Email :")
                to = receiver
                SendEmail(to, content)
                pyttsx3.speak(content)
                pyttsx3.speak("Email has been sent")

            except Exception as e:
                print(e)
                pyttsx3.speak("Unable to send")
