from Speak import speak
from TakeCommand import TakeCommand
import pywhatkit
import os
import random


def music():
    speak('You like to listen Online or Offline?')
    ans = TakeCommand().lower()
    if 'online' in ans:
        speak('What should I play for you?')
        ans = TakeCommand().lower()
        speak('playing ' + ans)
        pywhatkit.playonyt(ans)


    elif 'offline' in ans:

        songs_dir = 'C:\music'  # path-----------------------------
        music = os.listdir(songs_dir)
        speak('What should I play for you?')
        speak('Select a number....')
        ans = TakeCommand().lower()
        while 'number' not in ans and ans != 'random' and ans != 'you choose':
            speak('I could not understand you . Please try again.')
            ans = TakeCommand().lower()
        if 'number' in ans:
            no = int(ans.replace('number', ''))
        elif 'random' or 'you choose' in ans:
            no = random.randint(1, 100)
            os.startfile(os.path.join(songs_dir, music[no]))

