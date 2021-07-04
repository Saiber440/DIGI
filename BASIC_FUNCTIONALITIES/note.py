from CORE.TakeCommand import TakeCommand
from CORE.Speak import speak
import datetime
import os



def write_note():
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
        speak('I got your note ,Sir!')


def show_note():
    speak('Showing NOTES')
    file = open('notes.txt','r')
    print(file.read())
    speak(file.read())
