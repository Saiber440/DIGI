import remember
from Speak import speak
from TakeCommand import TakeCommand


def remember_that():
    speak("What should I remember Sir?")
    memory = TakeCommand()
    speak("You asked me to remember that" + memory)
    remember = open(('memory.txt', 'w'))
    remember.write(memory)
    remember.close()


def remember_anything():
    er = open('memory.txt', 'r')
    speak(' You asked me to remember that ' + remember.read())