import random
from CORE.Speak import speak


def roll():
    speak('Okay, rolling a die for you')
    die = ['1', '2', '3', '4', '5', '6']
    roll = []
    roll.extend(die)
    random.shuffle(roll)
    roll = (''.join(roll[0]))
    speak('I rolled a die and you got' + roll)
