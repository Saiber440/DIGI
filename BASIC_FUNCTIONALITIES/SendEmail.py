import smtplib

from Speak import speak
from CORE.TakeCommand import TakeCommand


def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('placementelites@gmail.com', 'placementelites@2021')
    server.sendmail('placementelites@gmail.com', to, content)
    server.close()


def tryout():
    speak("What should I say?")
    content = TakeCommand()
    speak("Who is the receiver?")
    receiver = input("Enter Receiver Email :")
    to = receiver
    SendEmail(to, content)
    speak(content)
    speak("Email has been sent")


def exception():
    print(exception)
    speak("Unable to send")