import os


def logout():
    os.system("shutdown -l")


def restart():
    os.system("shutdown /r /t 1")


def shutdown():
    os.system("shutdown /s /t 1")