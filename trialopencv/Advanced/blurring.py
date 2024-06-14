import cv2 as cv

img = cv.imread('/Users/aaditya/dev/learning /trialopencv/adi.png')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0) #sigma(x): std in x direction 
cv.imshow('Gaussian Blur', gauss)

# Median Blur, helps in reducing noise
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral, retains edges 
bilateral = cv.bilateralFilter(img, 10, 35, 25)        
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)