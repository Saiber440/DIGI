import pyttsx3
from SEARCH_FUNCTIONS import Chrome
from CORE.CloseJarvis import ExitYourself
from SEARCH_FUNCTIONS.SearchOnline import GoogleSearch, BingSearch
from BASIC_FUNCTIONALITIES.WeatherByPritam import WeatherTemp
from SEARCH_FUNCTIONS.YouTube import YouTubeSearch
from CORE.TakeCommand import TakeCommand
from SEARCH_FUNCTIONS.Wikipedia import wiki
from BASIC_FUNCTIONALITIES.SendEmail import tryout, exception
from BASIC_FUNCTIONALITIES.DateAndTime import date, time
from BASIC_FUNCTIONALITIES.batterycheck import BatteryInfo
# ====================================================
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wolframalpha_app_id = 'EJ3QJT-2YHHU3AYK7'
# ========================== Pritam Day =========================


if __name__ == '__main__':

    while True:
        # permission = TakeCommand()
        # if "wake up" in permission:
        #     WishMe()
        # elif "go to sleep" in permission:
        #     break
        # elif "goodbye" in permission:
        #     sys.exit()
        query = TakeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'battery' in query:
            BatteryInfo()

        elif 'wikipedia' in query:
            wiki()

        elif 'send email' in query:
            try:
                tryout()
            except:
                exception()

        elif 'search internet' in query:
            Chrome.ChromeSearch()

        elif 'search youtube' in query:
            YouTubeSearch()

        elif 'search Google' in query:
            GoogleSearch()

        elif 'search bing' in query:
            BingSearch()

        elif 'temperature' in query:
            WeatherTemp()

        elif 'stop' in query:
            ExitYourself()
