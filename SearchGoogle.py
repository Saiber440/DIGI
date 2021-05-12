from Speak import speak
from TakeCommand import TakeCommand
import webbrowser as wb

def GoogleSearch():
    speak('What to search?')
    search_Term = TakeCommand().lower()
    wb.open('https://google.com/search?q=' + search_Term)