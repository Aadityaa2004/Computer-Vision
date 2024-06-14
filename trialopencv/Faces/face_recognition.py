
import numpy as np 
import cv2 as cv

haar_cascade = cv.CascadeClassifier('/Users/aaditya/dev/learning /trialopencv/Faces/haar_face.xml')

people = ['BenAfflek', 'EltonJohn', 'JerrySeinfield', 'Madonna', 'MindyKaling']

features = np.load('/Users/aaditya/dev/learning /trialopencv/features.npy', allow_pickle=True)
labels = np.load('/Users/aaditya/dev/learning /trialopencv/labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread('/Users/aaditya/dev/learning /trialopencv/Resources/Faces/val/ben_afflek/3.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person-gray', gray)

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+h]
    
    labels, confidence = face_recognizer.predict(faces_roi)
    print(f' The person is {people[labels]}, with a confidence of {int(confidence)} %')