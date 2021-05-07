from Speak import speak
import pyttsx3
engine = pyttsx3.init()
import datetime


def WishMe():
    speak("WELCOME BACK PRITAM")
    datetime.time()
    # datetime.date()

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <=12:
        speak("Good Morning Pritam")
    elif hour >= 12 and hour <=18:
        speak("Good Afternoon Pritam")
    elif hour >= 18 and hour <=24:
        speak("Good Evening Pritam")
    else:
        speak("HAVE A GOOD DAY AHEAD PRITAM")

    speak("HI PRITAM, WHAT CAN I HELP YOU")
