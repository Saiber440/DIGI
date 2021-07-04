from CORE.Speak import speak
from CORE.TakeCommand import TakeCommand
import webbrowser as wb


def ChromeSearch():
    speak("What to search?")
    chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    search = TakeCommand().lower()
    wb.get(chromepath).open_new_tab(search + '.com')
