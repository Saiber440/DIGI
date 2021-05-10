import speech_recognition as sr


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising...")
        query = r.recognize_google(audio, language = 'en-US')
        print(query)

    except Exception as e:
        print(e)
        print("Can't recognise, try again...")
        return "None"
    return query
