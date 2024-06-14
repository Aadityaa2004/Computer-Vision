import cv2 as cv
import numpy as np
import os

# Ensure the path to haar_cascade is correct
haar_cascade_path = '/Users/aaditya/dev/learning /trialopencv/Faces/haar_face.xml'
if not os.path.exists(haar_cascade_path):
    print("Haar cascade file not found!")
    exit()

haar_cascade = cv.CascadeClassifier(haar_cascade_path)

cap = cv.VideoCapture(0)
cap.set(3, 160)  # Width
cap.set(4, 120)  # Height

if not cap.isOpened():
    print("Couldn't open Camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Frame not read")
        break

    if frame is None or frame.size == 0:
        print("Frame is empty")
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x, y, w, h) in faces_rect:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

    # Display the frame with detected faces
    cv.imshow('Detected face', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
