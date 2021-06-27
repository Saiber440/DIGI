from plyer import notification
import psutil
battery = psutil.sensors_battery()
percent = battery.percent

title = 'Battery Percentage Remaining is ' + str(percent) + '%'
message= 'Thankyou for reading! Take care!'

notification.notify(title= title,
                    message= message,
                    app_icon = None,
                    timeout= 10,
                    toast=False)
