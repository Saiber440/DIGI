import psutil
from pyttsx3 import speak


def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at' +usage)

    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)