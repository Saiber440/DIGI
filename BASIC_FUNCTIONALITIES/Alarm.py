# import os
import datetime
from playsound import playsound
from Speak import speak
# from TakeCommand import TakeCommand
# os. system('clear')
# speak("What hour do you want the alarm to ring? ")
# alarmH = TakeCommand()
# #alarmH = int(input("What hour do you want the alarm to ring? "))
# speak("What minute do you want the alarm to ring? ")
# alarmM = TakeCommand()
# #alarmM = int(input("What minute do you want the alarm to ring? "))
# speak("am or pm? ")
# amPm = TakeCommand()
# #amPm = str(input("am or pm? "))
# os.system('clear')
# print("Waiting for alarm",alarmH,alarmM,amPm)
# if (amPm == "pm"):
#         alarmH = alarmH + 12


def alarm(timing):
    altime = str(datetime.datetime.now().strptime(timing, "%I:%M %p"))
    altime = altime[11:-3]
    alarmH = altime[:2]
    alarmH = int(alarmH)
    alarmM = altime[3:5]
    alarmM = int(alarmM)
    speak("Alarm is set for"+str({timing}))
    print(f"Alarm is set for {timing}")
    while True:
        if alarmH == datetime.datetime.now().hour:
            if alarmM == datetime.datetime.now().minute:
                print("Time to wake up")
                speak("Time to wake up")
                playsound('C:\\Users\\bikra\\PycharmProjects\\JARVIS-ADVANCED\\alarm.mp3')
                break

            elif alarmM<datetime.datetime.now().minute:
                break


