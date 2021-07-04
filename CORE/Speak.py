from pyttsx3 import init
engine = init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()