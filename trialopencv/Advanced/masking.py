import cv2 as cv
import numpy as np

img = cv.imread('/Users/aaditya/dev/learning /trialopencv/adi.png')
cv.imshow('Adi', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

mask = cv.circle(blank.copy(), (img.shape[1]//2 - 90,img.shape[0]//2), 700, 1, -1) # the mmask can be shifted here itself 

# rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

# weird_shape = cv.bitwise_and(circle,rectangle)
# cv.imshow('Weird Shape', weird_shape)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('Weird Shaped Masked Image', masked)

cv.waitKey(0)