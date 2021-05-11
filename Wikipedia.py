from wikipedia import wikipedia

from Speak import speak


def wiki(query):
    speak("Searching...")
    query = query.replace("Wikipedia", "")
    result = wikipedia.summary(query, sentences=3)
    speak("According to Wikipedia")
    print(result)
    speak(result)