# import os
import datetime
from playsound import playsound
from CORE.Speak import speak


def alarm(timing):
    altime = str(datetime.datetime.now().strptime(timing, "%I:%M %p"))
    altime = altime[11:-3]
    alarmH = altime[:2]
    alarmH = int(alarmH)
    alarmM = altime[3:5]
    alarmM = int(alarmM)
    speak("Alarm is set for" + str({timing}))
    print(f"Alarm is set for {timing}")
    while True:
        if alarmH == datetime.datetime.now().hour:
            if alarmM == datetime.datetime.now().minute:
                print("Time to wake up")
                speak("Time to wake up")
                playsound('alarm_alarm.mp3')
                break

            elif alarmM < datetime.datetime.now().minute:
                break
