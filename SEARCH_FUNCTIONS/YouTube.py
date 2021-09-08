from CORE.Speak import speak
from CORE.TakeCommand import TakeCommand
import webbrowser as wb


def YouTubeSearch():
    speak('What to play?')
    search_Term = TakeCommand().lower()
    wb.open('https://youtube.com/results?search_query=' + search_Term)
