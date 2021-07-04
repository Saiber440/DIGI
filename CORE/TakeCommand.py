import speech_recognition as sr
from CORE.Speak import speak


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #r.listen(source,timeout=2)
        r.adjust_for_ambient_noise(source)
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
    query = query.lower()

    return query
