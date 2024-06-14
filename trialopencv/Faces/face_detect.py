import cv2 as cv

img = cv.imread('/Users/aaditya/dev/learning /trialopencv/lady.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray Person', gray)

haar_cascade = cv.CascadeClassifier('/Users/aaditya/dev/learning /trialopencv/Faces/haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)

cv.imshow('Detected Faces', img)

cv.imshow('lady', img)
cv.waitKey(0)



