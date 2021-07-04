import clipboard
from CORE.Speak import speak


def read():
    text = clipboard.paste()
    speak(text)
    print(text)

