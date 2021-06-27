import random
from Speak import speak


def flip():
    speak('Okay, flipping the coin')
    coin = ['heads', 'tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = (''.join(toss[0]))
    speak('I flipped the coin and you got' + toss)
