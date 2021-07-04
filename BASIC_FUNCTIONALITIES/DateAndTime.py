import datetime
from CORE.Speak import speak
import pyttsx3
engine = pyttsx3.init()



def time():
    Time = (datetime.datetime.now()).strftime("%I:%M %p")
    speak(f"The current time is: {Time}")


def date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    speak("The current date is")
    speak(day)
    speak(month)
    speak(year)
