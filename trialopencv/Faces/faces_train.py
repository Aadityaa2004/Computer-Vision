import os
import cv2 as cv 
import numpy as np 

people = ['BenAfflek', 'EltonJohn', 'JerrySeinfield', 'Madonna', 'MindyKaling']
DIR = '/Users/aaditya/dev/learning /trialopencv/Resources/Faces/train/'
haar_cascade = cv.CascadeClassifier('/Users/aaditya/dev/learning /trialopencv/Faces/haar_face.xml')

features = []
labels = []

def create_train():
    for folder in people:
        path = os.path.join(DIR, folder)
        label = people.index(folder)
        
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            
            img_array = cv.imread(img_path)
            if img_array is None:
                continue  # Skip if image not read properly
            
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

            for (x, y, w, h) in faces_rect:
                # We take the region of interest and append it to features
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

# creating a training data set 
create_train()

print(" ------------ Training Done ------------ ")

# making features and labels in array format
features = np.array(features, dtype='object')
labels = np.array(labels)

# Creating the face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Training the recognizer on the features and labels lists
face_recognizer.train(features, labels)

# saving the files 
face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)
