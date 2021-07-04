import os
from CORE.Speak import speak
from CORE.TakeCommand import TakeCommand


def app():
    speak('What should I open?')
    ans = TakeCommand().lower()
    if 'python' in ans:
        py_path = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.3\\bin\\pycharm64.exe'
        os.startfile(py_path)

    elif 'java' in ans:
        jvm_path = 'C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2020.2\\bin\\idea64.exe'
        os.startfile(jvm_path)

    elif 'chrome' in ans:
        chrm_path = 'C:\\Program Files\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.exe'
        os.startfile(chrm_path)

    elif 'notepad' in ans:
        nt_pad = 'C:\\Windows\\System32\\notepad.exe'
        os.startfile(nt_pad)

