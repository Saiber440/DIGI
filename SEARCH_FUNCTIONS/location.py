from CORE.Speak import speak
import webbrowser as wb

def locate(query):
    query = query.replace("where is", " ")
    location = query
    speak("User asked to locate " + location)
    wb.open_new_tab("https://www.google.com/maps/place" + location)