import speech_recognition as sr
from Speak import speak

def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        #audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language = 'en-IN')
        print(query)

    except Exception as e:
        print(e)
        print("Can't recognise, try again...")
        speak("Can't recognise, try again")
        return "None"

    return query
