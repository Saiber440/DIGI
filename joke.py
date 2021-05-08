import pyjokes
from pyttsx3 import speak


def joke():
    speak(pyjokes.get_joke(()))