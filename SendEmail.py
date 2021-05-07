import smtplib


def SendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('placementelites@gmail.com', 'placementelites@2021')
    server.sendmail('placementelites@gmail.com', to, content)
    server.close()
