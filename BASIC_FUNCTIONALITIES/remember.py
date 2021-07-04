from CORE.Speak import speak
import os


def remember_that(tc):
    # speak("What should I remember Sir?")
    # memory = TakeCommand()
    speak("You asked me to remember that" + tc)
    remember = open('memories.txt','w')
    remember.write(tc)
    remember.close()



def remember_anything():
    er = open('memories.txt','r')
    speak('You asked me to remember that' + er.read())
