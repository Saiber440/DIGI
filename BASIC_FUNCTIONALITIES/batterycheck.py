import psutil
from CORE.Speak import speak


def BatteryInfo():

    battery = psutil.sensors_battery()
    percent = battery.percent

    speak(f"you have {percent}% left")
    if percent < 75:
        speak("You should consider connecting your device to the charger")
