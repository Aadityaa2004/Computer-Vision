import cv2 as cv 
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8') # data type of an image 
# We are giving this the shape of width, height and the number of colour channels.  

while True:
    cv.imshow('Blank', blank)
    blank[200:300, 300:400] = 0,0,255
    cv.imshow('Green', blank)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cv.waitKey(0)


# Drawing Shapes and Putting text

# cv.rectangle
# cv.circle
# cv.line
# cv.putText



#  Essential finctions in Opencv

# cv.cvtColor() -> converting to grayscale
# cv.gaussianBlur -> blurs the image 
# cv.Canny -> edge Cascade
# cv.threshhold -> binarize an Image 
# cv.dilate -> thickens the edges
# cv.erode -> thins the edges
# cv.resize -> resizes the image
# cv.flip -> flips the image
# cv.imread -> reads the image
# cv.imwrite -> writes the image
# cv.copyMakeBorder -> adds a border to the image
# cv.addWeighted -> adds two images
# cv.bitwise_and -> bitwise and operation
# cv.bitwise_or -> bitwise or operation
# cv.bitwise_not -> bitwise not operation
# cv.bitwise_xor -> bitwise xor operation
# cv.split -> splits the image
# cv.merge -> merges the image



# Translations 


