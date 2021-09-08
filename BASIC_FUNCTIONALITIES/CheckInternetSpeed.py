import speedtest
from CORE.Speak import speak


def InternetSpeed():
    speak("Checking your Internet Speed...")
    st = speedtest.Speedtest()
    download = st.download()
    ds = download/1e+6
    dsinmbps = round(ds)
    upload = st.upload()
    us = upload / 1e+6
    usinmbps = round(us)
    speak(f"Your download speed is {dsinmbps} megabytes per second and your upload speed is {usinmbps} megabytes per second")