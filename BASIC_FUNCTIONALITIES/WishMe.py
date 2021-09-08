import time
from CORE.Speak import speak
import pyttsx3
engine = pyttsx3.init()
import datetime


def WishMe():
    speak("WELCOME BACK")
    datetime.time()
    # datetime.date()
    tt = time.strftime("%I:%M %p")

    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <=12:
        speak(f"A Very Good Morning To You. The current time is {tt}")
    elif hour >= 12 and hour <=16:
        speak(f"Good Afternoon! The current time is {tt}")
    elif hour >= 16 and hour <=24:
        speak(f"Good Evening. The current time is {tt}")
    else:
        speak("HAVE A GOOD DAY AHEAD")

    speak("HOW CAN I HELP YOU")