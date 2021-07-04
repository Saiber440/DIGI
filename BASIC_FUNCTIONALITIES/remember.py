from CORE.Speak import speak
from CORE.TakeCommand import TakeCommand


def remember_that(tc):
    # speak("What should I remember Sir?")
    # memory = TakeCommand()
    speak("You asked me to remember that" + tc)
    remember = open(('memory.txt', 'w'))
    remember.write(tc)
    remember.close()
    remember_anything(remember)


def remember_anything(remember):
    er = open('memory.txt', 'r')
    speak('You asked me to remember that' + remember.read(er))