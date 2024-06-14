import cv2 as cv 
import time 
import numpy as np
import Module as m
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

wCam, hCam = 640, 480
pTime = 0
cTime = 0
    
detector = m.handDetector()    

cap = cv.VideoCapture(0)

cap.set(3, wCam)
cap.set(4, hCam)

    
if not cap.isOpened():
    print("Couldn't open Camera")
    exit()

while True:
    ret, frame = cap.read()

    frame = detector.findHands(frame)

    lmList = detector.findPosition(frame, draw=False)
    if len(lmList) != 0:
        print(lmList[4])

    if not ret:
        print("Frame not read")
        break

    if frame is None or frame.size == 0:
        print("Frame is empty")
        break
           
    cTime = time.time()  # current Time
    fps = 1 / (cTime - pTime)  # calculating the fps
    pTime = cTime

    cv.putText(frame, f'FPS: {int(fps)}', (10, 30), fontScale=0.7, fontFace=cv.FONT_HERSHEY_COMPLEX, color=(10, 10, 10), thickness=2)  # printing the fps

    cv.imshow('detected Pose', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv.destroyAllWindows()