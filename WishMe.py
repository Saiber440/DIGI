from Speak import speak
import pyttsx3
engine = pyttsx3.init()
import datetime


def WishMe():
    speak("WELCOME BACK SIR")
    datetime.time()
    # datetime.date()

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <=12:
        speak("A Very Good Morning To You Sir")
    elif hour >= 12 and hour <=18:
        speak("Good Afternoon Sir!")
    elif hour >= 18 and hour <=24:
        speak("Good Evening Sir")
    else:
        speak("HAVE A GOOD DAY AHEAD SIR")

    speak("HOW CAN I HELP YOU")
