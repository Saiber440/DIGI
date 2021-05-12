from Speak import speak
from TakeCommand import TakeCommand
import time


def sleep():  # Not working
    speak('For how many seconds should I stop listening?')
    ans = int(TakeCommand())
    time.sleep(ans)
    print(ans)
