import clipboard
from Speak import speak


def read():
    text = clipboard.paste()
    speak(text)
    print(text)

