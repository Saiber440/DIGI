
from Speak import speak
from TakeCommand import TakeCommand
import webbrowser as wb


def ChromeSearch():
    speak("What to search?")
    chromepath = 'C:\Program Files\Google\Chrome\Application/chrome.exe'
    search = TakeCommand().lower()
    wb.get(chromepath).open_new_tab(search + '.com')