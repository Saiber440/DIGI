import os
from Speak import speak
from TakeCommand import TakeCommand




def app():
    speak('What should I open?')
    ans = TakeCommand().lower()
    if 'python' in ans:
        codepath = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
        os.startfile(codepath)

    elif 'java' in ans:
        codepath = 'C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2\\bin\\idea64.exe'
        os.startfile(codepath)
