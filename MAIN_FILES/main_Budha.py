import sys
import pyttsx3
#from SEARCH_FUNCTIONS import Chrome
from SEARCH_FUNCTIONS.SearchOnline import SearchOnline
from SEARCH_FUNCTIONS.YouTube import YouTubeSearch
from CORE.TakeCommand import TakeCommand
from SEARCH_FUNCTIONS.WikiHow import HowTo
from BASIC_FUNCTIONALITIES.WishMe import WishMe
from BASIC_FUNCTIONALITIES.SendEmail import tryout, exception
from BASIC_FUNCTIONALITIES.DateAndTime import date, time
from CORE.Speak import speak
from BASIC_FUNCTIONALITIES.calculate import calculate
from CORE.lrs import logout, restart, shutdown
import wolframalpha
# from sleep import sleep
from BASIC_FUNCTIONALITIES.whatsappMessage import WhatsAppMessage
from BASIC_FUNCTIONALITIES.ReadSelectedText import read
from BASIC_FUNCTIONALITIES.WeatherUpdates import weather
from BASIC_FUNCTIONALITIES.Alarm import alarm
from OPEN_APPS.Camera import Cam
from BASIC_FUNCTIONALITIES.batterycheck import BatteryInfo
from BASIC_FUNCTIONALITIES.screenshot import screenshot
from BASIC_FUNCTIONALITIES.note import write_note,show_note
from BASIC_FUNCTIONALITIES.cpu import cpu
from CORE.offline import offline
from BASIC_FUNCTIONALITIES.remember import remember_that,remember_anything
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from untitled import Ui_MainWindow
# ====================================================
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
wolframalpha_app_id = 'EJ3QJT-2YHHU3AYK7'
# ========================================


# ========================== Pritam Day =========================
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        self.TaskExecution()

# if __name__ == '__main__':
    def TaskExecution(self):
        WishMe()

        while True:

            self.query = self.TakeCommand().lower()

            if 'time' in self.query:
                time()

            elif 'date' in self.query:
                date()

            elif 'wikipedia' in self.query:
                HowTo()

            elif 'send email' in self.query:
                try:
                    tryout()
                except:
                    exception()

            # elif 'search internet' in self.query:
            #     Chrome.ChromeSearch()

            elif 'search youtube' in self.query:
                YouTubeSearch()

            elif 'battery' in self.query:
                BatteryInfo()

            elif 'cpu' in self.query:
                cpu()

            # elif 'search google' in self.query:
            #     GoogleSearch()

            elif 'screenshot' in self.query:
                screenshot()

            elif 'write a note' in self.query:
                write_note()

            elif 'show me notes' in self.query:
                show_note()


            # ============================= Budhaditya Sarkar ===================================

            elif 'calculate' in self.query:
                calculate(self.query)

            elif 'what is' in self.query:
                client = wolframalpha.Client(wolframalpha_app_id)
                res = client.self.query(self.query)
                try:
                    print(next(res.results).text)
                    speak(next(res.results).text)
                except StopIteration:
                    print("No Results")

            # elif 'stop Listening' in self.query: # Not Working
            #     sleep()

            elif 'logout' in self.query: # Logout, restart and shutdown not working
                logout()
            elif 'restart' in self.query:
                restart()
            elif 'shutdown' in self.query:
                shutdown()

            elif 'whatsapp message' in self.query:
                WhatsAppMessage()

            elif 'Weather' in self.query:
                weather()

            elif 'read' in self.query:
                read()

            elif 'alarm' in self.query:
                #speak("At what time should I set the alarm? For example set the alarm to 6:00 am")
                tt = self.query.replace("set the alarm to ", "")
                tt = tt.replace(".","")
                tt = tt.upper()
                alarm(tt)

            elif 'camera' in self.query:
                Cam()

            elif 'go offline' in self.query:
                offline()

            elif 'remember that' in self.query:

                tc = self.query.replace("remember that ", "")
                remember_that(tc)

            elif 'remember anything' in self.query:
                remember_anything()

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("Uhy5.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("ff0431d11ff6b73e937280252f58f371.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start()
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString(Qt.DefaultLocaleShortDate)
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)

app = QApplication(sys.argv)
digi = Main()
digi.show()
exit(app.exec_())
