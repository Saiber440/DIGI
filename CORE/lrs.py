import os


def logout():
    os.system("shutdown /l /t 0")


def restart():
    os.system("shutdown /r /t 0")


def shutdown():
    os.system("shutdown /s /t 0")