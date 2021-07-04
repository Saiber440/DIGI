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
    speak("Today is")
    if day == 1:
        speak("first of")
    elif day == 2:
        speak("second of")
    elif day == 3:
        speak("third of")
    elif day == 4:
        speak("fourth of")
    elif day == 5:
        speak("fifth of")
    elif day == 6:
        speak("sixth of")
    elif day == 7:
        speak("seventh of")
    elif day == 8:
        speak("eighth of")
    elif day == 9:
        speak("nineth of")
    elif day == 10:
        speak("tenth of")
    elif day == 11:
        speak("eleventh of")
    elif day == 12:
        speak("twelveth of")
    elif day ==13:
        speak("thirteeth of")
    elif day == 14:
        speak("fourteeth of")
    elif day == 15:
        speak("fifteenth of")
    elif day == 16:
        speak("sixteeth of")
    elif day == 17:
        speak("seventeeth of")
    elif day == 18:
        speak("eighteeth of")
    elif day == 19:
        speak("nineteeth of")
    elif day == 20:
        speak("twentieth of")
    elif day == 21:
        speak("twenty first of")
    elif day == 22:
        speak("twenty second of")
    elif day == 23:
        speak("twenty third of")
    elif day == 24:
        speak("twenty fourth of")
    elif day == 25:
        speak("twenty fifth of")
    elif day == 26:
        speak("twenty sixth of")
    elif day == 27:
        speak("twenty seventh of")
    elif day == 28:
        speak("twenty eighth of")
    elif day == 29:
        speak("twenty nineth of")
    elif day == 30:
        speak("thirtieth of")
    elif day == 31:
        speak("thirty first")

    if month == 1:
        speak("January")
    elif month == 2:
        speak("February")
    elif month == 3:
        speak("March")
    elif month == 4:
        speak("April")
    elif month == 5:
        speak("May")
    elif month == 6:
        speak("June")
    elif month == 7:
        speak("July")
    elif month == 8:
        speak("August")
    elif month == 9:
        speak("September")
    elif month == 10:
        speak("October")
    elif month == 11:
        speak("November")
    else:
        speak("December")
    speak(year)
