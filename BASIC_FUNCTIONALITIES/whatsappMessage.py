import webbrowser as wb
import pyautogui
from time import sleep
from CORE.Speak import speak
from CORE.TakeCommand import TakeCommand


def SendWhatsappMessage(phone_number, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone={'+phone_number+'}&text={'+Message+'}')
    sleep(10)
    pyautogui.press('enter')


def WhatsAppMessage():
    user_name= {
        'Jarvis':'+91 7003187066'
    }
    try:
        speak("To whom should I send?")
        name= TakeCommand()
        phone_number = user_name[name]
        message = TakeCommand()
        SendWhatsappMessage(phone_number,message)
        speak("Message has been sent")
    except Exception as e:
        print(e)
        speak("Unable to send the WhatsApp Message")