import pywikihow
from Speak import speak


def HowTo(query):
    speak("Here's how to do this")
    result = list(pywikihow.search_wikihow(query, max_results=10, lang='en'))
    assert len(result) == 1
    result[0].print()
    speak(result[0].summary)
