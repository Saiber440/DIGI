from Speak import speak
from CORE.TakeCommand import TakeCommand
import webbrowser as wb


def GoogleSearch():
    speak('What to search?')
    # search_Term = TakeCommand().lower()
    # wb.open('https://google.com/search?q=' + search_Term)
    cm = TakeCommand().lower()
    wb.open(f"{cm}")


def BingSearch():
    speak('What to search?')
    search_Term = TakeCommand().lower()
    wb.open('https://bing.com/search?q=' + search_Term)
