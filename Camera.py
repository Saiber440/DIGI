import cv2

def Cam():
    cam = cv2.VideoCapture(0)
    while cam.isOpened():
        ret, frame = cam.read()
        if cv2.waitKey(10) == ord('q'):
            break
        cv2.imshow('My Cam', frame)