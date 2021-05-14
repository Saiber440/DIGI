from Speak import speak
import os


def word():
    speak('Opening MS word...')
    ma_word = r' ==============================.exe'  # path for the app
    os.startfile(ma_word)