import pywhatkit
from wikipedia import wikipedia
from Speak import speak
from CORE.TakeCommand import TakeCommand


def SearchOnline():
    speak('What to search?')
    searching_term = TakeCommand().lower()
    speak("Searching...")
    searching_term = searching_term.replace("Wikipedia", "")
    searching_term = searching_term.replace("Search", "")
    searching_term = searching_term.replace("Search Wikipedia", "")
    searching_term = searching_term.replace("Search Google", "")
    pywhatkit.search(searching_term)

    try:
        result = wikipedia.summary(searching_term, sentences=3)
        print(result)
        speak(result)
    except:
        speak("These are the results found on the Internet")


# def ChromeSearch():
#     speak("What to search?")
#     chromepath = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
#     search = TakeCommand().lower()
#     wb.get(chromepath).open_new_tab(search + '.com')

# def GoogleSearch():
#     speak('What to search?')
#     search_Term = TakeCommand().lower()
#     wb.open('https://google.com/search?q=' + search_Term)
#
#
# def BingSearch():
#     speak('What to search?')
#     search_Term = TakeCommand().lower()
#     wb.open('https://bing.com/search?q=' + search_Term)